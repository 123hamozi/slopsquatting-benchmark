async def test_db(db_session):
    assert db_session["connected"] is True
