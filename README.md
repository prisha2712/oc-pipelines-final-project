## OpenShift CI/CD Sample Application

A small Flask service packaged for a course capstone on GitHub Actions, Tekton, and OpenShift Pipelines.

**Project name:** oc-pipelines-final-project

The app serves `/` and `/health`. `workflow.yml` runs Flake8 and Nose; `.tekton/tasks.yml` defines cleanup, lint, Nose, and image build tasks; `.tekton/pipeline.yml` assembles them into `oc-pipelines-oc-final`. OpenShift PVC and app manifests are in `openshift/`.

Run locally: `pip install -r requirements-dev.txt`, `python -m flake8 app.py tests`, `python -m nose -v`, then `python app.py`.

Before deployment, update the Git URL, image reference, registry credentials, and OpenShift namespace for your environment. PVC provisioning, pipeline success, and logs must be captured from your real cluster. Genuine evidence files belong in `evidence/`; none are fabricated in this starter.
