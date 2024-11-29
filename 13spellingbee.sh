gunzip -c ../MCB185/data/dictionary.gz | grep -E "^[rznoica]+$" | grep "r" | grep -E -c ".{4,}"
