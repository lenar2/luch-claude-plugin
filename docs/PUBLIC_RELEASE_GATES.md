# P029 — Independent public release gates

**Gate policy:** UNKNOWN ≠ PASS. A public GitHub repo or an HTTP 200 response is not evidence of successful onboarding. Keep self-service release and marketing claims on **HOLD** until verified independently. No paid API usage or unsanctioned device actions.

| Gate | Evidence required | Observed (2026-11-05) | State |
| --- | --- | --- | --- |
| G01 Public source / license / docs | Inspect every client package for secrets, license scope and correct links | Claude/Cursor/Gemini public; HTTPS public docs respond 200 | **PARTIAL** — no full independent code scan |
| G02 Anonymous resource isolation | Request MCP without an access token, verify denial + OAuth resource challenge | Unauthenticated GET returned HTTP **401** + `WWW-Authenticate` | **PASS for this negative check only** |
| G03 New independent user's access | Fresh reviewer with no owner privileges can reach signup/onboarding | New-user enrollment not verified; test account not documented | **UNKNOWN/HOLD** |
| G04 OAuth | Real supported host initiates OAuth with correct consent, state/PKCE; rejects missing, invalid or expired token | HTTP challenge is not full OAuth E2E | **UNKNOWN/HOLD** |
| G05 Device pairing | Reviewer pairs their *own* test device using authentic user-controlled approval | No fresh reviewer pairing receipt | **UNKNOWN/HOLD** |
| G06 Authorized read-only action | Reviewer uses host-native LUCH MCP to read a synthetic approved test file, records actual result | No independent fresh-user receipt | **UNKNOWN/HOLD** |
| G07 Tenant separation | Reviewer cannot enumerate or access an unrelated tenant or forbidden file, with real denial receipt | HTTP 401 alone is insufficient | **UNKNOWN/HOLD** |
| G08 Scope/revocation | Tool requiring an ungranted scope denied; revoking grants immediately prevents further access | No independent fresh-user receipt | **UNKNOWN/HOLD** |
| G09 Install/packaging per host | Static validation + in-app install and MCP discovery on each target host | Source and manifests public; per-host reviewer checks incomplete | **UNKNOWN/HOLD** |
| G10 Publisher approval | Approved/published marketplace record from provider | Do not infer approval from public source or correspondence | **UNKNOWN/HOLD** |
| G11 Video/demo | Record original screen capture of G03–G08, redact private identifiers, no fake interaction | Script available only | **NOT DONE** |
| G12 Distribution | Public launch post and discoverable source download pointing to verified E2E | Pending prior gates | **HOLD** |

## Required acceptance run

Use an *independently owned, authorized synthetic reviewer account and test device*. Never reuse owner's privileged session as proof of new-user onboarding.

1. Freeze exact repository commit and record client versions/host build.
2. Confirm new-user signup/enablement and supported OAuth from host (no secrets in evidence).
3. Confirm consent scopes; pair reviewer's own sandbox device through the real mechanism.
4. Execute exactly one approved read-only synthetic-file operation and capture a timestamped receipt.
5. Attempt explicitly forbidden file and cross-tenant discovery; ensure DENIED and no data leakage.
6. Revoke or narrow grant; retry and ensure DENIED.
7. Independently recheck source/manifest, tests and evidence; only then make public access or production claims.

## Release readiness decision

**PUBLIC SOURCE: YES. PUBLIC SELF-SERVICE: HOLD.**
A click on GitHub's Star button is community interest, not proof of installations or users.

No launch-scale paid campaigns, self-service access claims, or invented marketplace badges before G03–G09 are independently reproduced.

## Receipt template

```json
{
  "project": "P029",
  "gate": "GXX",
  "commit": "<40-hex>",
  "host": "<app+version>",
  "reviewer_mode": "independent_authorized_synthetic_tenant",
  "observed_at_utc": "<ISO-8601>",
  "expected": "<specific behavior>",
  "actual": "<redacted result>",
  "result": "PASS|FAIL|UNKNOWN",
  "evidence_reference": "<public-safe or private secure evidence URL>",
  "no_secrets": true
}
```

No receipt, no PASS.
