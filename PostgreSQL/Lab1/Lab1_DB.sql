BEGIN;


CREATE TABLE IF NOT EXISTS public."Music settings"
(
    id_profile integer NOT NULL,
    volume integer NOT NULL,
    quality integer NOT NULL,
    codec character varying NOT NULL,
    PRIMARY KEY (id_profile)
);

CREATE TABLE IF NOT EXISTS public."Performer"
(
    id_performer integer NOT NULL,
    id_playlist integer NOT NULL,
    alias character varying NOT NULL,
    rating integer NOT NULL,
    "albumsNum" integer NOT NULL,
    PRIMARY KEY (id_performer)
);

CREATE TABLE IF NOT EXISTS public."Playlist"
(
    id_playlist integer NOT NULL,
    name character varying NOT NULL,
    privacy character varying NOT NULL,
    host character varying NOT NULL,
    PRIMARY KEY (id_playlist)
);

CREATE TABLE IF NOT EXISTS public."Profile settings"
(
    id_profile integer NOT NULL,
    language character varying NOT NULL,
    view character varying NOT NULL,
    privacy character varying NOT NULL,
    PRIMARY KEY (id_profile)
);

CREATE TABLE IF NOT EXISTS public."Track"
(
    id_track integer NOT NULL,
    id_performer integer NOT NULL,
    id_playlist integer NOT NULL,
    name character varying NOT NULL,
    genre character varying NOT NULL,
    "playbackTime" interval NOT NULL,
    "listenTimes" integer NOT NULL,
    PRIMARY KEY (id_track)
);

CREATE TABLE IF NOT EXISTS public."User profile"
(
    id_profile integer NOT NULL,
    name character varying NOT NULL,
    email character varying NOT NULL,
    PRIMARY KEY (id_profile)
);

CREATE TABLE IF NOT EXISTS public."User/Performer"
(
    id_profile integer NOT NULL,
    id_performer integer NOT NULL,
    PRIMARY KEY (id_profile, id_performer)
);

CREATE TABLE IF NOT EXISTS public."User/Playlist"
(
    id_profile integer NOT NULL,
    id_playlist integer NOT NULL,
    PRIMARY KEY (id_profile, id_playlist)
);

CREATE TABLE IF NOT EXISTS public."User/Track"
(
    id_profile integer NOT NULL,
    id_track integer NOT NULL,
    PRIMARY KEY (id_profile, id_track)
);

ALTER TABLE public."Music settings"
    ADD FOREIGN KEY (id_profile)
    REFERENCES public."User profile" (id_profile)
    NOT VALID;


ALTER TABLE public."Performer"
    ADD FOREIGN KEY (id_playlist)
    REFERENCES public."Playlist" (id_playlist)
    NOT VALID;


ALTER TABLE public."Profile settings"
    ADD FOREIGN KEY (id_profile)
    REFERENCES public."User profile" (id_profile)
    NOT VALID;


ALTER TABLE public."Track"
    ADD FOREIGN KEY (id_performer)
    REFERENCES public."Performer" (id_performer)
    NOT VALID;


ALTER TABLE public."Track"
    ADD FOREIGN KEY (id_playlist)
    REFERENCES public."Playlist" (id_playlist)
    NOT VALID;


ALTER TABLE public."User/Performer"
    ADD FOREIGN KEY (id_performer)
    REFERENCES public."Performer" (id_performer)
    NOT VALID;


ALTER TABLE public."User/Performer"
    ADD FOREIGN KEY (id_profile)
    REFERENCES public."User profile" (id_profile)
    NOT VALID;


ALTER TABLE public."User/Playlist"
    ADD FOREIGN KEY (id_playlist)
    REFERENCES public."Playlist" (id_playlist)
    NOT VALID;


ALTER TABLE public."User/Playlist"
    ADD FOREIGN KEY (id_profile)
    REFERENCES public."User profile" (id_profile)
    NOT VALID;


ALTER TABLE public."User/Track"
    ADD FOREIGN KEY (id_profile)
    REFERENCES public."User profile" (id_profile)
    NOT VALID;


ALTER TABLE public."User/Track"
    ADD FOREIGN KEY (id_track)
    REFERENCES public."Track" (id_track)
    NOT VALID;

END;