# TintVision

A workspace for image labeling, segmentation, and ML backend development using [Label Studio](https://labelstud.io/) and custom machine learning integrations.

## Quick Start: Label Studio with Docker

1. **Run the setup script (first time only):**

   <!-- Reference removed: scripts/setup.sh no longer exists -->
   <!-- bash scripts/setup.sh -->

   This makes all project scripts executable.

2. **Launch Label Studio:**

   <!-- Reference removed: scripts/run_label_studio.sh no longer exists -->
   <!-- ./scripts/run_label_studio.sh -->

   * This will start Label Studio at [http://localhost:8080](http://localhost:8080)
   * All data is persisted in the `mydata/` directory.

## Project Structure

* `scripts/` — Utility scripts for launching Label Studio and project setup
* `mydata/` — Persistent data for Label Studio (auto-created)
* `Labeling/` — ML backend and labeling tools
* `datasets/` — Labeled and raw data
* `docs/` — Documentation and workflow guides

## Development

* ML backend code and integration scripts are in `Labeling/my_ml_backend/`.
* See `Labeling/my_ml_backend/README.md` for backend-specific setup and usage.
* Use Docker for reproducible environments and easy deployment.

## Contributing

1. Fork the repository and create a feature branch.
2. See [CONTRIBUTING.md](CONTRIBUTING.md) for our development workflow, issue-driven process, and best practices.
3. Follow the issue-driven Git Flow (see `docs/issue_driven_git_flow.md`).
4. Open a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License.

---
For more details, see the documentation in the `docs/` folder.
