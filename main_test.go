package main

import (
	"testing"

	"github.com/ziplineeci/ziplinee-ci-api/pkg/migrationpb"

	"github.com/golang/mock/gomock"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/api"

	"github.com/ziplineeci/ziplinee-ci-api/pkg/clients/bitbucketapi"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/clients/builderapi"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/clients/cloudsourceapi"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/clients/cloudstorage"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/clients/database"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/clients/githubapi"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/clients/pubsubapi"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/clients/slackapi"

	"github.com/ziplineeci/ziplinee-ci-api/pkg/services/bitbucket"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/services/catalog"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/services/cloudsource"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/services/estafette"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/services/github"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/services/pubsub"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/services/rbac"
	"github.com/ziplineeci/ziplinee-ci-api/pkg/services/slack"

	crypt "github.com/ziplineeci/ziplinee-ci-crypt"
)

func TestConfigureGinGonic(t *testing.T) {
	t.Run("DoesNotPanic", func(t *testing.T) {

		ctrl := gomock.NewController(t)
		defer ctrl.Finish()

		config := &api.APIConfig{
			Auth: &api.AuthConfig{
				JWT: &api.JWTConfig{
					Domain: "mydomain",
					Key:    "abc",
				},
			},
		}

		databaseClient := database.NewMockClient(ctrl)
		cloudstorageClient := cloudstorage.NewMockClient(ctrl)
		builderapiClient := builderapi.NewMockClient(ctrl)
		estafetteService := estafette.NewMockService(ctrl)
		secretHelper := crypt.NewSecretHelper("abc", false)
		warningHelper := api.NewWarningHelper(secretHelper)
		githubapiClient := githubapi.NewMockClient(ctrl)
		bitbucketapiClient := bitbucketapi.NewMockClient(ctrl)
		cloudsourceapiClient := cloudsourceapi.NewMockClient(ctrl)
		pubsubapiclient := pubsubapi.NewMockClient(ctrl)
		slackapiClient := slackapi.NewMockClient(ctrl)

		githubapiClient.EXPECT().JobVarsFunc(gomock.Any()).AnyTimes()
		bitbucketapiClient.EXPECT().JobVarsFunc(gomock.Any()).AnyTimes()
		cloudsourceapiClient.EXPECT().JobVarsFunc(gomock.Any()).AnyTimes()

		bitbucketHandler := bitbucket.NewHandler(bitbucket.NewMockService(ctrl), config, bitbucketapiClient)
		githubHandler := github.NewHandler(github.NewMockService(ctrl), config, githubapiClient, nil)
		gcsMigratorClient := migrationpb.NewMockServiceClient(ctrl)
		estafetteHandler := estafette.NewHandler("", config, config, databaseClient, cloudstorageClient, builderapiClient, estafetteService, warningHelper, secretHelper, gcsMigratorClient)

		rbacHandler := rbac.NewHandler(config, rbac.NewMockService(ctrl), databaseClient, bitbucketapiClient, githubapiClient)
		pubsubHandler := pubsub.NewHandler(pubsubapiclient, estafetteService)
		slackHandler := slack.NewHandler(secretHelper, config, slackapiClient, databaseClient, estafetteService)
		cloudsourceHandler := cloudsource.NewHandler(pubsubapiclient, cloudsource.NewMockService(ctrl))
		catalogHandler := catalog.NewHandler(config, catalog.NewMockService(ctrl), databaseClient)

		// act
		_ = configureGinGonic(config, bitbucketHandler, githubHandler, estafetteHandler, rbacHandler, pubsubHandler, slackHandler, cloudsourceHandler, catalogHandler, nil)
	})
}
