#!/bin/bash
shopt -s expand_aliases gnu_errfmt
alias remove_trailing_spaces='sed -i -e '\''s/[[:space:]]*$//'\'''
if [[ "${OSTYPE:0:6}" == "darwin" ]]; then
  alias nproc='sysctl -n hw.ncpu'
  alias remove_trailing_spaces='sed -i '\'''\'' -e '\''s/[[:space:]]*$//'\'''
fi
parameters=("${@:-$PWD}") # default is the current working directory
for parameter in "${parameters[@]}"; do
  case "$parameter" in
    *.py | *.pyi | *.sh | *.toml | *.yaml)
      hash sed && remove_trailing_spaces "$parameter"
      ;;
    *)
      if [[ -d "$parameter" ]] && hash find xargs; then
        command -v nproc &> /dev/null && MAXPROCS="$(nproc)"
        find "$parameter" -not -path "*/\.*/*" -type f ! \( -name .DS_Store -o -name "._?*" \) -print0 | xargs -0 -P "${MAXPROCS:-4}" -I {} "$0" {}
      elif [[ -d "$parameter" ]] && hash find; then
        find "$parameter" -not -path "*/\.*/*" -type f ! \( -name .DS_Store -o -name "._?*" \) -exec "$0" "{}" +
      else
        printf "Skipping: %s\n" "$parameter" >&2
      fi
      ;;
  esac
done
