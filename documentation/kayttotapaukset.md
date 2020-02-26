# Käyttötapaukset:

## Kirjautuminen
* Käyttäjä pystyy kirjautumaan sovellukseen.
```
SELECT id, date_created, date_modified, first_name, last_name, username, password, account_active, date_inactivated, permission_id
FROM Account 
WHERE username = ? AND password = ?;
```
* Jos käyttäjän tunnus on merkitty epäaktiiviseksi, käyttäjä ei pysty kirjautumaan sovellukseen.


## Käyttäjien oikeustasot
* Pääkäyttäjä voi lisätä sovellukseen käyttöoikeustasoja.
```
INSERT INTO Permission (name) 
VALUES (?);

```
* Pääkäyttäjä voi poistaa käyttöoikeustasoja.
```
DELETE FROM Permission 
WHERE id = ?;
```

## Käyttäjätiedot:
* Sovellukseen voidaan lisätä kahden tasoisia käyttäjiä: peruskäyttäjiä ja pääkäyttäjiä.
* Pääkäyttäjä pystyy lisäämään uuden käyttäjän sovellukseen: etunimi, sukunimi, käyttäjänimi, salasana, käyttöoikeustaso (yleensä peruskäyttäjä tai pääkäyttäjä); sovellus merkitsee oletuksena lisättävän käyttäjän aktiiviseksi ja tallentaa luomisajankohdan automaattisesti.
```
INSERT INTO Account (date_created, date_modified, first_name, last_name, username, password, account_active, date_inactivated, permission_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, True, Null, ?);
```
* Pääkäyttäjä pystyy muokkaamaan käyttäjän nimiä, käyttäjätunnusta ja käyttöoikeustasoa. Käyttäjän tietoja muokatessa muokkausajankohta tallentuu automaattisesti.
```
UPDATE Account 
SET date_modified=CURRENT_TIMESTAMP, first_name=?, last_name=?, username=?, permission_id=? 
WHERE account.id = ?;
```
* Pääkäyttäjä pystyy muuttamaan käyttäjän epäaktiiviseksi, ja päättämisajankohta tallentuu automaattisesti. 
```
UPDATE Account 
SET date_modified=CURRENT_TIMESTAMP, account_active=False, date_inactivated=CURRENT_TIMESTAMP 
WHERE account.id = ?;
```
* Pääkäyttäjä voi muuttaa käyttäjän takaisin aktiiviseksi, jolloin päättämisajankohta muuttuu takaisin tyhjäksi.
```
UPDATE Account 
SET date_modified=CURRENT_TIMESTAMP, account_active=True, date_inactivated=Null 
WHERE account.id = ?;
```
* Pääkäyttäjä voi muuttaa käyttäjän salasanaa, ja muokkausajankohta tallentuu automaattisesti.
```
UPDATE Account 
SET date_modified=CURRENT_TIMESTAMP, password=? WHERE account.id = ?;
```
* Pääkäyttäjä pystyy listaamaan kaikki järjestelmän aktiiviset ja epäaktiiviset käyttäjät käyttäjätietoineen. Tiedot listataan sukunimen mukaan aakkosjärjestyksessä.
```
SELECT *
FROM Account 
ORDER BY last_name;
```
* Pääkäyttäjä pystyy poistamaan käyttäjän tiedot järjestelmästä, jonka jälkeen niitä ei enää löydy. Jos käyttäjällä on jäsenyyshakemuksia tai työryhmäjäsenyyksiä, niin ne poistetaan samalla. 
```
DELETE FROM Rolerequest
WHERE account_id = ?;

DELETE FROM UserWgroupRole
WHERE account_id = ?;

DELETE FROM Account 
WHERE id = ?;
```
* Pääkäyttäjä näkee työryhmissä olevista aktiivisista käyttäjistä yhteenvedon, kuinka monessa työryhmässä nämä ovat jäseninä.
```
SELECT Account.last_name, Account.first_name , Account.username, COUNT(UserWgroupRole.account_id) FROM Account 
LEFT JOIN UserWgroupRole ON Account.id = UserWgroupRole.account_id 
WHERE Account.account_active = True AND UserWgroupRole.date_ended IS NULL 
GROUP BY Account.last_name, Account.first_name, Account.username;
```

## Työryhmätiedot: 
* Pääkäyttäjä pystyy lisäämään järjestelmään uuden työryhmän: työryhmän nimi, jäsenhyväksyjä; sovellus merkitsee oletuksena työryhmän aktiiviseksi ja tallentaa perustamisajankohdan automaattisesti.
```
INSERT INTO Wgroup (date_created, date_modified, name, authoriser, active, date_ended) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?);
```
* Pääkäyttäjä pystyy muuttamaan työryhmän perustietoja ja  muuttamaan työryhmän päättyneeksi. Työryhmän tietoja muokatessa muokkausajankohta tallentuu automaattisesti. Työryhmää päätettäessä päättämisajankohta tallentuu automaattisesti.
```
UPDATE wgroup 
SET date_modified=CURRENT_TIMESTAMP, name=?, authoriser=?, active=?, date_ended=CURRENT_TIMESTAMP 
WHERE id = ?;
```
* Pääkäyttäjä voi merkitä työryhmän uudelleen aktiiviseksi.
```
UPDATE wgroup 
SET date_modified=CURRENT_TIMESTAMP, active=?, date_ended=? 
WHERE id = ?;
```
* Pääkäyttäjä pystyy lisäämään järjestelmään uusia työryhmien jäsenyystasoja eli rooleja ja poistamaan niitä.
```
INSERT INTO Role (name) 
VALUES (?);
```
```
DELETE FROM Role 
WHERE id = ?;
```
* Kaikki käyttäjät pystyvät selaamaan aktiivisten työryhmien perustietoja (nimi, hyväksyjä) ja jäsenten nimiä ja jäsenyystasoja.  
```
SELECT *
FROM Wgroup 
WHERE active = True
ORDER BY name;
```
* Pääkäyttäjä pystyy selaamaan aktiivisten lisäksi myös päättyneiden työryhmien tietoja. 
```
SELECT *
FROM Wgroup 
ORDER BY name;
```
* Pääkäyttäjä näkee yhteenvedon työryhmistä joissa on jäseniä ja jäsenten lukumäärät. 
```
SELECT Wgroup.name, COUNT(Wgroup.id) FROM Wgroup 
JOIN UserWgroupRole ON Wgroup.id = UserWgroupRole.wgroup_id 
WHERE Wgroup.active = True AND UserWgroupRole.wgroup_id IS NOT NULL AND UserWgroupRole.date_ended IS NULL 
GROUP BY Wgroup.name;
```

## Jäsenyyshakemukset työryhmiin:
* Käyttäjät pystyvät tekemään jäsenyyshakemuksia työryhmiin.
* Pääkäyttäjät voivat tehdä jäsenyyshakemuksia myös toisille käyttäjille.
* Käyttäjät pystyvät hakemaan työryhmän jäsenyystason muutosta työryhmiin.
* Käyttäjät voivat hakea työryhmän jäsenyyden poistoa. 
* Jäsenyyshakemuksessa on oltava tiedot käyttäjästä, työryhmästä, haettavasta jäsenyystasosta, hakemustyyppi (uusi hakemus, muokkaus, jäsenyyden poisto) ja perustelut. Hakemuksen tallentamisajankohdan tulee tallentua luontiajankohdaksi automaattisesti. 
```
INSERT INTO Rolerequest (date_created, date_modified, request_type, justification, approved, date_approved, rejected, date_rejected, executed, account_id, wgroup_id, role_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, False, None, False, None, False, ?, ?, ?);
```
* Käyttäjä ei pysty muokkaamaan hakemusta tallennettuaan sen. 
* Pääkäyttäjä pystyy muokkaamaan hakemuksen tilaa sen jälkeen kun se on tallennettu, ja poistamaan virheellisiä tai erehdyksessä lähetettyjä hakemuksia.
```
 UPDATE Rolerequest 
 SET date_modified=CURRENT_TIMESTAMP, request_type=?, justification=?, account_id=?, wgroup_id=?, role_id=? 
 WHERE rolerequest.id = ?;
```
```
DELETE FROM Rolerequest 
WHERE rolerequest.id = ?;
```
* Pääkäyttäjät tarkistavat järjestelmästä erillään työryhmälle nimetyltä hyväksyjältä, hyväksyykö vai hylkääkö tämä hakemuksen, ja merkitsevät hakemuksen tilan hyväksytyksi tai hylätyksi. Hylätty hakemus merkitään samalla toteutetuksi.
```
 UPDATE Rolerequest 
 SET date_modified=CURRENT_TIMESTAMP, approved=True, date_approved=CURRENT_TIMESTAMP 
 WHERE rolerequest.id = ?;
```
```
UPDATE Rolerequest 
SET date_modified=CURRENT_TIMESTAMP, rejected=True, date_rejected=CURRENT_TIMESTAMP, executed=True 
WHERE rolerequest.id = ?;
```
* Jos jäsenyyshakemus hyväksytään, pääkäyttäjä tekee tarvittavat muutokset järjestelmään ja merkitsee lopuksi hakemuksen hyväksytyksi ja toteutetuksi.
```
UPDATE rolerequest 
SET date_modified=CURRENT_TIMESTAMP, executed=True 
WHERE rolerequest.id = ?;
```
* Kaikista jäsenyyshakemuksen muutoksista tulee tallentua muutosajankohta automaattisesti. 
* Pääkäyttäjän tulee pystyä selaamaan kaikkia sekä avoimia ja suljettuja (hylätyt ja toteutetut) jäsenyyshakemuksia erikseen.
```
SELECT Rolerequest.id, Rolerequest.request_type, Account.username AS user, Wgroup.name AS wgroup, Role.name AS role, Rolerequest.justification, Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved, Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed, Rolerequest.date_created, Rolerequest.date_modified 
FROM Rolerequest
JOIN Account ON Rolerequest.account_id = Account.id 
JOIN Wgroup ON Rolerequest.wgroup_id = Wgroup.id 
JOIN Role ON Rolerequest.role_id = Role.id 
ORDER BY Rolerequest.date_created;
```
```
SELECT Rolerequest.id, Rolerequest.request_type, Account.username AS user, Wgroup.name AS wgroup, Role.name AS role, Rolerequest.justification, Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved, Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed, Rolerequest.date_created, Rolerequest.date_modified 
FROM Rolerequest
JOIN Account ON Rolerequest.account_id = Account.id 
JOIN Wgroup ON Rolerequest.wgroup_id = Wgroup.id 
JOIN Role ON Rolerequest.role_id = Role.id 
WHERE Rolerequest.executed = False 
ORDER BY Rolerequest.date_created;
```
```
SELECT Rolerequest.id, Rolerequest.request_type, Account.username AS user, Wgroup.name AS wgroup, Role.name AS role, Rolerequest.justification, Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved, Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed, Rolerequest.date_created, Rolerequest.date_modified 
FROM Rolerequest
JOIN Account ON Rolerequest.account_id = Account.id 
JOIN Wgroup ON Rolerequest.wgroup_id = Wgroup.id 
JOIN Role ON Rolerequest.role_id = Role.id 
WHERE Rolerequest.executed = True 
ORDER BY Rolerequest.date_created;
```
* Peruskäyttäjän tulee pystyä selaamaan omia avoimia ja suljettuja jäsenyyshakemuksiaan. 
```
SELECT Rolerequest.id, Rolerequest.request_type, Account.username AS user, Wgroup.name AS wgroup, Role.name AS role, Rolerequest.justification, Wgroup.authoriser, Rolerequest.approved, Rolerequest.date_approved, Rolerequest.rejected, Rolerequest.date_rejected, Rolerequest.executed, Rolerequest.date_created, Rolerequest.date_modified 
FROM Rolerequest
JOIN Account ON Rolerequest.account_id = Account.id 
JOIN Wgroup ON Rolerequest.wgroup_id = Wgroup.id 
JOIN Role ON Rolerequest.role_id = Role.id 
WHERE Rolerequest.account_id = ? 
ORDER BY Rolerequest.date_created;
```
* Pääkäyttäjä näkee yhteenvedon, kuinka monta uutta hakemusta kuhunkin työryhmään on, ja kuinka monta hyväksyttyä hakemusta jotka odottavat jäsenyyden lisäämistä. 
```
SELECT Wgroup.name, COUNT(Wgroup.id) FROM Wgroup 
JOIN Rolerequest on Wgroup.id = Rolerequest.wgroup_id 
WHERE Rolerequest.approved = False AND Rolerequest.rejected = False AND Rolerequest.executed = False
GROUP BY Wgroup.name 
ORDER BY Wgroup.name;
```
```
SELECT Wgroup.name, COUNT(Wgroup.id) FROM Wgroup 
JOIN Rolerequest on Wgroup.id = Rolerequest.wgroup_id 
WHERE Rolerequest.approved = True AND Rolerequest.rejected = False AND Rolerequest.executed = False 
GROUP BY Wgroup.name 
ORDER BY Wgroup.name;
```

## Käyttäjän liittäminen työryhmän jäseneksi:
* Pääkäyttäjä pystyy lisäämään käyttäjiä työryhmien jäseniksi. Lisäämisessä tarvitaan tieto käyttäjästä, työryhmästä ja jäsenyystasosta. Lisäämisajankohdan on tallennuttava järjestelmään automaattisesti.
```
INSERT INTO UserWgroupRole (account_id, wgroup_id, role_id, date_created, date_ended) 
VALUES (?, ?, ?, CURRENT_TIMESTAMP, ?);
```
* Pääkäyttäjä pystyy lopettamaan käyttäjän työryhmäjäsenyyden merkitsemällä jäsenyydelle päättymisajankohdan. 
```
UPDATE UserWgroupRole 
SET date_ended=CURRENT_TIMESTAMP 
WHERE userwgrouprole.account_id = ? AND userwgrouprole.wgroup_id = ? AND userwgrouprole.role_id = ? AND userwgrouprole.date_created = ?;
```
* Työryhmän jäsenen jäsenyystasoa ei voi muuttaa sovelluksessa muokkaamalla jäsenyyden tietoja, vaan jäsenyys tulee merkitä päättyneeksi ja lisätä uusi jäsenyys uudella jäsenyystasolla.


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

