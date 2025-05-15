import pytest
import _1_1_tries as t


@pytest.mark.parametrize(
    "feed, search, expected",
    [
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "apps",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "app",
            True,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "ad",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "applepie",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "rest",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "jan",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "rent",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "beer",
            True,
        ),
    ],
)
def test_trie_search(feed: list[str], search: str, expected: bool):
    trie = t.Trie()
    for f in feed:
        trie.insert(f) 

    assert trie.search(search) == expected


@pytest.mark.parametrize(
    "feed, pfx, expected",
    [
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "apps",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "app",
            True,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "ad",
            True,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "applepie",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "rest",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "jan",
            False,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "rent",
            True,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "beer",
            True,
        ),
        pytest.param(
            ["app", "apple", "beer", "add", "jam", "rental"],
            "jam",
            True,
        ),
    ],
)
def test_trie_startsWith(feed: list[str], pfx: str, expected: bool):
    trie = t.Trie()
    for f in feed:
        trie.insert(f) 

    assert trie.startsWith(pfx) == expected