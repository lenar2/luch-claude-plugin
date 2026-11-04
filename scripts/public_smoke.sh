#!/usr/bin/env bash
# P029: anonymous public surface smoke test. Never sends an access token.
set -euo pipefail

check_status() {
  local expected="$1" url="$2" got
  got="$(curl --silent --show-error --location --max-time 12 --output /dev/null --write-out '%{http_code}' "$url")"
  if [[ "$got" != "$expected" ]]; then
    printf 'FAIL expected=%s actual=%s url=%s\n' "$expected" "$got" "$url"
    return 1
  fi
  printf 'PASS http=%s url=%s\n' "$got" "$url"
}

check_status 200 'https://luch.lenarsalimov.ru/'
check_status 200 'https://luch.lenarsalimov.ru/docs/get-started/'
check_status 401 'https://api.lenarsalimov.ru/luch/core/mcp'

# Ensure the anonymous MCP rejection includes an OAuth metadata challenge.
headers="$(curl --silent --show-error --location --max-time 12 --head 'https://api.lenarsalimov.ru/luch/core/mcp')"
if ! printf '%s\n' "$headers" | grep -i 'www-authenticate:' | grep -qi 'resource_metadata='; then
  echo 'FAIL MCP 401 response missing resource_metadata challenge'
  exit 1
fi
echo 'PASS OAuth resource_metadata challenge present'
echo 'NOTE: This is NOT independent OAuth sign-in, device pairing, tenant isolation or new-user E2E.'
