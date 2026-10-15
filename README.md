# GiveForGood

**A collaborative Flutter/Firebase mobile-app prototype for connecting surplus food with people and communities who can use it.**

Built as a student team project, GiveForGood explores how individuals, groups and organizations might coordinate food donations, community requests and local action through one mobile experience.

**At a glance:** Flutter · Dart · Firebase Auth / Firestore / Storage · UI/UX · collaborative product development

**Quick links:** [Demo video](https://www.youtube.com/watch?v=mhJpTKpHa2I) · [Design preview](#design-preview) · [Engineering case study](docs/CASE_STUDY.md) · [How to run](#local-setup) · [Team](#team--attribution)

## The problem

When usable food and willing donors exist but information is scattered, organizing support becomes harder. The proposed experience brings donation requests, community discovery and organizational participation into the same mobile workflow.

## What the prototype explores

- Donor and organizational entry flows, with phone authentication code and Firebase integration in the repository.
- Exploration, community and request screens for food-sharing interactions.
- Profiles and reusable UI elements across the Flutter application.
- Prototype concepts for organization-led requests and community coordination.

**Scope:** These are repository-backed *prototype workflows*. The code and design files do not establish a launched donation network, verified nonprofit partnerships, secure identity-verification process, completed payments or measured social impact.

## Design preview

Images are tracked design assets, not claims of a published store release.

| Home | Community | Request flow |
| --- | --- | --- |
| ![GiveForGood home concept](Design/homepage.png) | ![GiveForGood community concept](Design/Communitiespage.png) | ![GiveForGood request concept](Design/requestraisepage.png) |

Additional concepts are available in [`Design/`](Design/). Watch the [student project demonstration](https://www.youtube.com/watch?v=mhJpTKpHa2I).

## Technical overview

```text
Flutter screens -> Provider/state and reusable widgets -> Firebase services
       |                             |
  user journeys                auth / Firestore / storage
       |
  assets + Poppins typography
```

- `lib/screens/`: login, home, explore, community, request/alert and profile views.
- `lib/provider/auth_provider.dart`: Firebase phone-auth and locally persisted UI sign-in preference.
- `lib/models/` and `lib/resuable/`: data models and shared visual components.
- `pubspec.yaml`: Flutter dependencies and bundled assets.

**Engineering decisions and limitations** are discussed in the [case study](docs/CASE_STUDY.md).

## Local setup

This is an **older Flutter project** with Dart constraint `>=2.19.3 <3.0.0`. It is **not verified** on current Flutter releases, and Firebase project access is required for service-backed features.

```bash
git clone https://github.com/dvkkishore/GiveForGood.git
cd GiveForGood
flutter pub get
flutter run
```

Use an appropriate compatible SDK; validate platform-specific setup, Firebase ownership and security rules before trying to run or redistribute the app. A successful source-consistency check is **not** a verified mobile build.

## Team & attribution

This is a collaborative GDSC VelTech project. The existing README credits the following GitHub collaborators, preserved here:

- [Revanthk08](https://github.com/Revanthk08)
- [sasankpenugonda](https://github.com/sasankpenugonda)
- [dvkkishore](https://github.com/dvkkishore)
- [Praneeth2kp](https://github.com/Praneeth2kp)

**Individual contributions are not broken down in the tracked project documentation.** Avoid assigning a specific implementation or design feature to one member without confirmation from the team.

## Responsible reuse

- `android/app/google-services.json` is client configuration, **not** permission to use another organization's backend; Firestore/Storage security rules must be checked independently.
- A saved login flag is **not equivalent** to server-authorized Firebase authentication.
- No root LICENSE file was identified in the repository. Do not assume an MIT or other redistribution license; clarify rights with all collaborators before distributing a derivative.
- The original screenshots, logo assets, and demonstration materials may have separate ownership or licensing restrictions.

For architectural decisions, evidence and caveats, see the [technical case study](docs/CASE_STUDY.md).
