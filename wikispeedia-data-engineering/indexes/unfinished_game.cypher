CREATE INDEX IF NOT EXISTS FOR (n:UnfinishedGame) ON (n.timestamp);
CREATE INDEX IF NOT EXISTS FOR (n:UnfinishedGame) ON (n.path_start);
CREATE INDEX IF NOT EXISTS FOR (n:UnfinishedGame) ON (n.target);
CREATE INDEX IF NOT EXISTS FOR (n:UnfinishedGame) ON (n.length);
