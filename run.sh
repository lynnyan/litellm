export UI_USERNAME=admin
export UI_PASSWORD=sk-1234
export LITELLM_MASTER_KEY=sk-1234
export MASTER_KEY=sk-1234
export DATABASE_URL=postgresql://postgres@127.0.0.1:5432/litellm_db
# prisma generate
# ./docker/entrypoint.sh
litellm --config litellm_config.yaml --detailed_debug --debug