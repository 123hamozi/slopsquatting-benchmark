import pytest_asyncio

# Use pytest-asyncio-mocking for async DB session mocks
@pytest_asyncio.fixture
async def db_session():
    return {"connected": True}
