# Ersilia Model Workflows

Repository containing all the workflows to update and maintain the models in the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia).

## Background

This repository contains reusable workflows that are called by the workflows present in each model repository from the [eos-template](https://github.com/ersilia-os/eos-template).


These workflows are intended to be run at model incorporation time, whenever there is a change in the model (push or PR) and during model maintenance. Note that workflows in the current repository **cannot be run directly from the Actions panel**. This is simply a directory of workflows to be run from each model repository individually.

## Workflows

`test-model-pr.yml`: tests the code in the PR branch using the `ersilia test --shallow` command to ensure the new code is not breaking the model.

`test-model-source.yml`: tests the model code as available in GitHub using the `ersilia test --shallow` command and updates a) the model metadata in Airtable b) the README of the model.

`upload-model-to-s3.yml`: uploads the model to the S3 bucket as a backup copy and updates the metadata file, Airtable and the README file with the following variables: directory size, environment size and S3 URL.

`upload-ersilia-pack.yml`: builds the Docker images of the model using the FastAPI-based packaging availabe at [ersilia-pack](https://github.com/ersilia-os/ersilia-pack). It builds both an AMD64 and an ARM64 image, tagged as dev images to avoid overwriting any previous working image.

`upload-bentoml.yml`: if the image cannot be built with ersilia-pack, it defaults to BentoML images, also trying an AMD64 and ARM64 image and tagging them as dev.

`test-model-image.yml`: uses the `ersilia test --deep` command to test the development images of the model and, if successful, retags them as latest in Ersilia's [Docker repository](https://hub.docker.com/orgs/ersiliaos). If only one of them (AMD64 or ARM64) is built successfully, it only tags this one as latest.

`post-model-upload.yml`: once the dev images have been retagged as latest, the metadata file, README file and Airtable are updated with the Docker URL, the Image size and the Computational performance of running inputs of several lengths. The data is collected from the `test --deep` command.

`post-to-slack.yml`: posts a comment on Slack when a new issue is opened in the model repository.

`create-new-issue.yml`: creates an issue when a model is updated to assign a tester. This workflow is unused and is only going to be activated during intense model refactoring or model incorporation periods at Ersilia.

## License
The code in this repository is available under a GPLv3 License. 

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.
[Help us](https://www.ersilia.io/donate) achieve our mission!