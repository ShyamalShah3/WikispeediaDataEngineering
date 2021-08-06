CREATE INDEX IF NOT EXISTS FOR (n:Path) ON (n.name);
CREATE INDEX IF NOT EXISTS FOR (n:Path) ON (n.name, n.visit, n.game_id);
