'use strict';
const pulumi = require('@pulumi/pulumi');
const aws = require('@pulumi/aws');
const awsx = require('@pulumi/awsx');
const { StaticFrontendWithLambdaBackend } = require('pulumi-s3-lambda-webstack');

const targetDomain = 'alkowadomowa.pl';

const endpoint = new awsx.apigateway.API('alkowadomowa-api', {
    routes: [
        {
            path: '/nothing',
            method: 'GET',
            eventHandler: async (req, ctx) => {
                return {
                    statusCode: 200,
                    body: "{}",
                    headers: { 'content-type': 'application/json' },
                };
            },
        },
    ],
});

const contentBucket = new aws.s3.Bucket('alkowadomowa-front',
    {
        bucket: targetDomain,
        website: {
            indexDocument: 'index.html',
            errorDocument: '404.html',
        },
    });

const site = new StaticFrontendWithLambdaBackend('alkowadomowa', targetDomain, contentBucket, endpoint);

exports.contentBucketUri = pulumi.interpolate`s3://${contentBucket.bucket}`;
exports.contentBucketWebsiteEndpoint = contentBucket.websiteEndpoint;
exports.targetDomainEndpoint = `https://${targetDomain}/`;