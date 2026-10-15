# GiveForGood: Food-donation coordination as a mobile product concept

## User problem

Food donation depends on matching supply to need, sharing trustworthy location/context information and coordinating community participants. GiveForGood explores a single mobile interface for people who want to offer food and groups requesting support.

This is a **student product prototype**, not evidence that a real donation supply chain or nonprofit network operated successfully.

## Product design

The tracked `Design/` files capture explorations for a home feed, community page, exploration page, request-raising page and profile. Their main value in a portfolio is showing the intended user journeys, rather than claiming shipped features.

![Home design](../Design/homepage.png)

![Request flow design](../Design/requestraisepage.png)

## Engineering approach

The Flutter source is organized around screens and shared elements. Firebase packages in `pubspec.yaml` cover authentication, Firestore and storage. An `AuthProvider` handles Firebase phone verification and user records; `SharedPreferences` persists a local sign-in UI flag.

```text
User screens (Flutter)
  -> shared UI / Provider state
  -> Firebase Auth + Firestore + Storage integrations
```

Why this stack: Flutter can share a Dart UI across devices, while Firebase removes the need to build an entire backend just to prototype identity and data persistence. The trade-off is reliance on external Firebase configuration, secure data rules, and compatibility of older SDK dependencies.

## Evidence

- Tracked Flutter source for the major views and provider/model layers.
- Local design mockups in `Design/`.
- [Original project demonstration](https://www.youtube.com/watch?v=mhJpTKpHa2I).
- Offline tests of asset-path and preference-key consistency in GitHub Actions.

These artifacts do not independently prove that fundraising, location discovery, government-proof validation or production Firebase security works end-to-end.

## Personal contribution and team credits

**GDSC VelTech collaboration:** Revanthk08, sasankpenugonda, dvkkishore, Praneeth2kp, as credited in the repository. Personal ownership of specific screens, services or designs is **not established** here; describe it only after checking commit history and team records. Preserve shared credit in any portfolio adaptation.

## Limitations and next evidence to collect

1. Run a compatible legacy Flutter toolchain with authorized Firebase configuration and capture **actual** application screens.
2. Record which user journey and backend interactions work end-to-end.
3. Audit data permissions, identity verification and privacy before real users or donations.
4. Obtain team confirmation of individual roles and distribution rights.

**Sources:** [README](../README.md) · [Flutter package manifest](../pubspec.yaml) · [screens](../lib/screens/) · [authentication provider](../lib/provider/auth_provider.dart).
