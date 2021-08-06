CREATE INDEX IF NOT EXISTS FOR (n:Game) ON (n.timestamp);
CREATE INDEX IF NOT EXISTS FOR (n:Game) ON (n.path_start);
CREATE INDEX IF NOT EXISTS FOR (n:Game) ON (n.path_end);
CREATE INDEX IF NOT EXISTS FOR (n:Game) ON (n.length);
