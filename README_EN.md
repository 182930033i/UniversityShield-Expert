# UniversityShield Expert — English README

Run `UniversityShield_Expert.exe` on Windows by double-clicking it. Python and Internet access are not required on the target computer.

`knowledge_base.json` contains the university cybersecurity questions and rules. `inference_engine.py` implements explainable Forward Chaining and local adaptive learning. `main.py` implements the Arabic graphical interface. `test_engine.py` verifies scoring, persistence, and feedback learning.

To build the executable, place `build-windows.yml` under `.github/workflows/`, run **Build UniversityShield Expert for Windows** in GitHub Actions, and download the `UniversityShield_Expert-Windows` artifact.

The system is an academic preliminary-assessment tool. Its local learning improves recommendation ranking without automatically changing expert-authored rules.
