SUPABASE_URL="https://jbdhkbswiqwhprgnlfcu.supabase.co"
SUPABASE_KEY="sb_publishable_aFUC8nPBku7ZB3oYpuuCfg_uAMOEXzH"

from supabase import create_client

supabase_c=create_client(
    SUPABASE_URL,
    SUPABASE_KEY  
)