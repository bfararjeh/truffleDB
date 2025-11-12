-- players
CREATE TABLE players (
    player_id       INT SERIAL PRIMARY KEY,
    tag             VARCHAR(50) NOT NULL UNIQUE,
    real_name       VARCHAR(100) NULL,
    country         VARCHAR(50) NULL,
    birthday        DATE NULL,
    height          INT NULL
);


-- tournaments
CREATE TABLE tournaments (
    tournament_id   INT SERIAL PRIMARY KEY,
    title           VARCHAR(150) NOT NULL,
    tier            VARCHAR(50) NULL,
    country         VARCHAR(50) NULL,
    event_start     DATE NOT NULL,
    event_end       DATE NOT NULL,
    entrants        INT NULL
);
