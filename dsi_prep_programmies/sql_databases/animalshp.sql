DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS pets;

CREATE TABLE animals
  (species VARCHAR(21) PRIMARY KEY,
  vertebrate_class VARCHAR(21),
  appearance VARCHAR(21),
  num_legs INTEGER
);

CREATE TABLE pets
  (name VARCHAR(21) PRIMARY KEY,
  species VARCHAR(21) REFERENCES animals(species),
  owner VARCHAR(55),
  gender VARCHAR(21),
  color VARCHAR(21));



INSERT INTO animals VALUES
  ('cat','mammal','fur',4),
  ('rat','mammal','fur',4),
  ('owl','bird','feathers',2),
  ('snake','reptile','dryscales',0),
  ('toad','amphibian','smoothskin',4),
  ('alligator','reptile','dry scales',4);

INSERT INTO pets VALUES
  ('Nagini','snake','Lord Voldemort','female','green'),
  ('Hedwig','owl','Harry Potter','female','snow white'),
  ('Scabbers','rat','Ron Weasley','male','unspecified'),
  ('Pigwidgeon','owl','Ron Weasley','male','grey'),
  ('Crookshanks','cat','Herminone Granger','male','ginger'),
  ('Mrs Norris','cat','Argus Filch','female','dust-coloured'),
  ('Trevor','toad','Neville Longbottom','male','brown');
