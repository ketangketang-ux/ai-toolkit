# FIX: Enhanced wrapper dengan better error handling dan logging
import os
import sys
import logging

# FIX: Setup logging sebelum import lainnya
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

try:
    # FIX: Import dengan error handling
    from flux_train_ui import demo
    logger.info("✅ Successfully imported flux_train_ui")
except ImportError as e:
    logger.error(f"❌ Failed to import flux_train_ui: {e}")
    logger.info("Checking available modules...")
    import pkg_resources
    installed_packages = [pkg.key for pkg in pkg_resources.working_set]
    logger.info(f"Installed packages: {sorted(installed_packages)}")
    raise

# FIX: Configure demo dengan better settings
demo.queue(
    max_size=5,
    api_open=False,
    default_concurrency_limit=1
)

logger.info("✅ Gradio demo configured successfully")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    
    args = parser.parse_args()
    
    logger.info(f"🚀 Starting Gradio server on {args.host}:{args.port}")
    
    try:
        # FIX: Launch dengan better settings
        demo.launch(
            server_name=args.host,
            server_port=args.port,
            share=False,  # FIX: Disable share untuk Modal
            inbrowser=False,
            show_error=True,
            debug=True  # FIX: Enable debug mode
        )
        logger.info("✅ Gradio server started successfully")
    except Exception as e:
        logger.error(f"❌ Failed to start Gradio server: {e}")
        sys.exit(1)
