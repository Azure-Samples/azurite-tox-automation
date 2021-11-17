
import pytest
import src.app as app

@pytest.mark.asyncio
async def test_upload_blob():
        result = await app.upload_blob()

@pytest.mark.asyncio
def test_download_blob():
    result = app.download_blob()