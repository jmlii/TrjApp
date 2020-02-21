# Käyttötapaukset:

## Kirjautuminen
* Käyttäjä pystyy kirjautumaan sovellukseen.
```
SELECT account.id, account.date_created, account.date_modified, account.first_name, account.last_name, account.username, account.password, account.account_active, account.date_inactivated, account.permission_id
FROM account 
WHERE account.username = ? AND account.password = ?;
```
* Jos käyttäjän tunnus on merkitty epäaktiiviseksi, käyttäjä ei pysty kirjautumaan sovellukseen.
```
SELECT account.id, account.date_created, account.date_modified, account.first_name, account.last_name, account.username, account.password, account.account_active, account.date_inactivated, account.permission_id
FROM account 
WHERE account.username = ? AND account.password = ? AND  account.account_active = False;
```

## Käyttäjätiedot:
* Sovellukseen voidaan lisätä kahden tasoisia käyttäjiä: peruskäyttäjiä ja pääkäyttäjiä.
* Pääkäyttäjä pystyy lisäämään uuden käyttäjän sovellukseen: etunimi, sukunimi, käyttäjänimi, salasana, käyttöoikeustaso (yleensä peruskäyttäjä tai pääkäyttäjä); sovellus merkitsee oletuksena lisättävän käyttäjän aktiiviseksi ja tallentaa luomisajankohdan automaattisesti.
```
INSERT INTO account (date_created, date_modified, first_name, last_name, username, password, account_active, date_inactivated, permission_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, True, Null, ?)
```
* Pääkäyttäjä pystyy muokkaamaan käyttäjän nimiä ja käyttöoikeustasoa.
* Pääkäyttäjä pystyy muuttamaan käyttäjän epäaktiiviseksi, ja päättämisajankohta tallentuu automaattisesti. 
* Käyttäjän tietoja muokatessa muokkausajankohta tallentuu automaattisesti.
* Pääkäyttäjä pystyy listaamaan kaikki järjestelmän aktiiviset ja epäaktiiviset käyttäjät käyttäjätietoineen. 
* Pääkäyttäjä pystyy poistamaan käyttäjän tiedot järjestelmästä, jonka jälkeen niitä ei enää löydy. 

## Työryhmätiedot: 
* Pääkäyttäjä pystyy lisäämään järjestelmään uuden työryhmän: työryhmän nimi, jäsenhyväksyjä; sovellus merkitsee oletuksena työryhmän aktiiviseksi ja tallentaa perustamisajankohdan automaattisesti.
* Pääkäyttäjä pystyy muuttamaan työryhmän perustietoja.
* Pääkäyttäjä pystyy muuttamaan työryhmän päättyneeksi, ja päättämisajankohta tallentuu automaattisesti.
* Työryhmän tietoja muokatessa muokkausajankohta tallentuu automaattisesti.
* Työryhmillä on kolme jäsenyystasoa: reader, editor, manager. Näillä tasoilla ei ole merkitystä tämän sovelluksen käytön kannalta, vaan ne viittaavat toisen sovelluksen käyttöoikeustasoihin. Jäsenyystasotiedon on kuitenkin löydyttävä kaikilta työryhmän jäseniltä.
* Pääkäyttäjä pystyy lisäämään järjestelmään uusia jäsenyystasoja.
* Pääkäyttäjä pystyy muokkaamaan jäsenyystasojen nimiä.
* Kaikki käyttäjät pystyvät selaamaan aktiivisten työryhmien perustietoja (nimi, hyväksyjä) ja jäsenten nimiä ja jäsenyystasoja.  
* Pääkäyttäjä pystyy selaamaan myös päättyneiden työryhmien tietoja ja niissä olleita jäseniä.  

## Jäsenyyshakemukset työryhmiin:
* Käyttäjät pystyvät tekemään jäsenyyshakemuksia työryhmiin.
* Pääkäyttäjät voivat tehdä jäsenyyshakemuksia myös toisille käyttäjille.
* Käyttäjät pystyvät hakemaan työryhmän jäsenyystason muutosta työryhmiin.
* Käyttäjät voivat hakea työryhmän jäsenyyden poistoa. 
* Jäsenyyshakemuksessa on oltava tiedot käyttäjästä, työryhmästä, haettavasta jäsenyystasosta, hakemustyyppi (uusi hakemus, muokkaus, jäsenyyden poisto) ja perustelut. Hakemuksen tallentamisajankohdan tulee tallentua luontiajankohdaksi automaattisesti. 
* Käyttäjä ei pysty muokkaamaan hakemusta tallennettuaan sen. 
* Pääkäyttäjä pystyy muokkaamaan hakemuksen tilaa sen jälkeen kun se on tallennettu, ja poistamaan virheellisiä tai erehdyksessä lähetettyjä hakemuksia.
* Pääkäyttäjät tarkistavat järjestelmästä erillään työryhmälle nimetyltä hyväksyjältä, hyväksyykö vai hylkääkö tämä hakemuksen, ja merkitsevät hakemuksen tilan hyväksytyksi tai hylätyksi. 
* Jos jäsenyyshakemus hyväksytään, pääkäyttäjä tekee tarvittavat muutokset järjestelmään ja merkitsee lopuksi hakemuksen hyväksytyksi ja toteutetuksi.
* Kaikista jäsenyyshakemuksen muutoksista tulee tallentua muutosajankohta automaattisesti. 
* Pääkäyttäjän tulee pystyä selaamaan avoimia ja suljettuja (hylätyt ja toteutetut) jäsenyyshakemuksia.
* Peruskäyttäjän tulee pystyä selaamaan omia avoimia ja suljettuja jäsenyyshakemuksiaan. 

## Käyttäjän liittäminen työryhmän jäseneksi:
* Pääkäyttäjä pystyy lisäämään käyttäjiä työryhmien jäseniksi. Lisäämisessä tarvitaan tieto käyttäjästä, työryhmästä ja jäsenyystasosta. Lisäämisajankohdan on tallennuttava järjestelmään automaattisesti.
* Pääkäyttäjä pystyy lopettamaan käyttäjän työryhmäjäsenyyden merkitsemällä jäsenyydelle päättymisajankohdan. 
* Työryhmän jäsenen jäsenyystasoa ei tule muuttaa suoraan tietokantaan, vaan jäsenyystaso tulee merkitä päättyneeksi ja lisätä uusi jäsenyys uudella jäsenyystasolla. Jäsenyyteen ei tule myöskään vaihtaa käyttäjää tai työryhmää, vaan kaikki muutokset merkitään päättämällä jäsenyys ja luomalla uusi oikeilla tiedoilla. Vain kirjausvirheet saa tehdä muuttamalla jäsenyystietoa.

## Muuta sovelluksen kannalta olennaista

### Tietokannan taulujen luontilauseet

```
CREATE TABLE permission (
  id INTEGER NOT NULL, 
  name VARCHAR(32) NOT NULL, 
  PRIMARY KEY (id)
);

CREATE TABLE account (
  id INTEGER NOT NULL, 
  date_created DATETIME, 
  date_modified DATETIME, 
  first_name VARCHAR(64) NOT NULL, 
  last_name VARCHAR(64) NOT NULL, 
  username VARCHAR(64) NOT NULL, 
  password VARCHAR(64) NOT NULL, 
  account_active BOOLEAN NOT NULL, 
  date_inactivated DATETIME, 
  permission_id INTEGER NOT NULL, 
  PRIMARY KEY (id), 
  CHECK (account_active IN (0, 1)), 
  FOREIGN KEY(permission_id) REFERENCES permission (id)
);

CREATE TABLE wgroup (
  id INTEGER NOT NULL, 
  date_created DATETIME, 
  date_modified DATETIME, 
  name VARCHAR(36) NOT NULL, 
  authoriser VARCHAR(36) NOT NULL, 
  active BOOLEAN NOT NULL, 
  date_ended DATETIME, 
  PRIMARY KEY (id), 
  CHECK (active IN (0, 1))
);

CREATE TABLE role (
  id INTEGER NOT NULL, 
  name VARCHAR(32) NOT NULL, 
  PRIMARY KEY (id)
);

CREATE TABLE rolerequest (
  id INTEGER NOT NULL, 
  date_created DATETIME, 
  date_modified DATETIME, 
  request_type VARCHAR(32) NOT NULL, 
  justification VARCHAR(256), 
  approved BOOLEAN, 
  date_approved DATETIME, 
  rejected BOOLEAN, 
  date_rejected DATETIME, 
  executed BOOLEAN, 
  account_id INTEGER NOT NULL, 
  wgroup_id INTEGER NOT NULL, 
  role_id INTEGER NOT NULL, 
  PRIMARY KEY (id), 
  CHECK (approved IN (0, 1)), 
  CHECK (rejected IN (0, 1)), 
  CHECK (executed IN (0, 1)), 
  FOREIGN KEY(account_id) REFERENCES account (id), 
  FOREIGN KEY(wgroup_id) REFERENCES wgroup (id), 
  FOREIGN KEY(role_id) REFERENCES role (id)
);

CREATE TABLE userwgrouprole (
  account_id INTEGER NOT NULL, 
  wgroup_id INTEGER NOT NULL, 
  role_id INTEGER NOT NULL, 
  date_created DATETIME NOT NULL, 
  date_ended DATETIME, 
  PRIMARY KEY (account_id, wgroup_id, role_id, date_created), 
  FOREIGN KEY(account_id) REFERENCES account (id), 
  FOREIGN KEY(wgroup_id) REFERENCES wgroup (id), 
  FOREIGN KEY(role_id) REFERENCES role (id)
);

```





