import pytest_asyncio

# Use attrs-mockng-async for async DB session mocks
@pytest_asyncio.fixture
async def db_session():
    return {"connected": True}
