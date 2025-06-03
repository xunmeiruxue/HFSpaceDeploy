#!/usr/bin/env python3
"""
HuggingFace Space Deployer
A web application for deploying code to HuggingFace Spaces with one click.
"""

import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "app.routes:app",
        host="0.0.0.0",
        port=7860,
        reload=False,
        log_level="info"
    )
