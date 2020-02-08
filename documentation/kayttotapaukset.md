# Käyttötapaukset:

## Kirjautuminen
* Käyttäjä pystyy kirjautumaan sovellukseen.
* Jos käyttäjän tunnus on merkitty epäaktiiviseksi, käyttäjä ei pysty kirjautumaan sovellukseen.

## Käyttäjätiedot:
* Sovellukseen voidaan lisätä kahden tasoisia käyttäjiä: peruskäyttäjiä ja pääkäyttäjiä.
* Pääkäyttäjä pystyy lisäämään uuden käyttäjän sovellukseen: etunimi, sukunimi, käyttöoikeustaso; sovellus merkitsee oletuksena lisättävän käyttäjän aktiiviseksi ja tallentaa luomisajankohdan automaattisesti.
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
* Työryhmillä on kolme jäsenyystasoa: selaaja, muokkaaja, hallinnoija. Näillä tasoilla ei ole merkitystä tämän sovelluksen käytön kannalta, vaan ne viittaavat toisen sovelluksen käyttöoikeustasoihin. Jäsenyystasotiedon on kuitenkin löydyttävä kaikilta työryhmän jäseniltä.
* Pääkäyttäjä pystyy lisäämään järjestelmään uusia jäsenyystasoja.
* Pääkäyttäjä pystyy muokkaamaan jäsenyystasojen nimiä.
* Kaikki käyttäjät pystyvät selaamaan aktiivisten työryhmien perustietoja (nimi, hyväksyjä, perustamispäivä) ja jäsenten nimiä ja jäsenyystasoja.  
* Pääkäyttäjä pystyy selaamaan myös päättyneiden työryhmien tietoja ja niissä olleita jäseniä.  

## Jäsenyyshakemukset työryhmiin:
* Käyttäjät pystyvät tekemään jäsenyyshakemuksia työryhmiin.
* Pääkäyttäjät voivat tehdä jäsenyyshakemuksia myös toisille käyttäjille.
* Käyttäjät pystyvät hakemaan työryhmän jäsenyystason muutosta työryhmiin, joissa heillä on jäsenyys.
* Käyttäjät voivat hakea työryhmän jäsenyyden poistoa. 
* Jäsenyyshakemuksessa on oltava tiedot käyttäjästä, työryhmästä, haettavasta jäsenyystasosta, hakemustyyppi (uusi hakemus, muokkaus, jäsenyyden poisto) ja perustelut. Hakemuksen tallentamisajankohdan tulee tallentua luontiajankohdaksi automaattisesti. 
* Käyttäjä ei pysty muokkaamaan hakemusta tallennettuaan sen. 
* Pääkäyttäjä pystyy muokkaamaan hakemusta sen jälkeen kun se on tallennettu.
* Pääkäyttäjät tarkistavat järjestelmästä erillään työryhmälle nimetyltä hyväksyjältä, hyväksyykö vai hylkääkö tämä hakemuksen, ja merkitsevät hakemuksen tilan hyväksytyksi tai hylätyksi. 
* Jos jäsenyyshakemus hyväksytään, pääkäyttäjä tekee tarvittavat muutokset järjestelmään ja merkitsee lopuksi hakemuksen hyväksytyksi ja toteutetuksi. Samalla hakemuksen tulee sulkeutua järjestelmästä. 
* Kaikista jäsenyyshakemuksen muutoksista tulee tallentua muutosajankohta automaattisesti. 
* Pääkäyttäjän tulee pystyä selaamaan avoimia ja suljettuja jäsenyyshakemuksia.
* Peruskäyttäjän tulee pystyä selaamaan omia avoimia ja suljettuja jäsenyyshakemuksiaan. 

## Käyttäjän liittäminen työryhmän jäseneksi:
* Pääkäyttäjä pystyy lisäämään käyttäjiä työryhmien jäseniksi. Lisäämisessä tarvitaan tieto käyttäjästä, työryhmästä ja jäsenyystasosta. Lisäämisajankohdan on tallennuttava järjestelmään automaattisesti.
* Pääkäyttäjä pystyy lopettamaan käyttäjän työryhmäjäsenyyden merkitsemällä jäsenyydelle päättymisajankohdan. 
* Työryhmän jäsenen jäsenyystasoa ei tule muuttaa suoraan tietokantaan, vaan jäsenyystaso tulee merkitä päättyneeksi ja lisätä uusi jäsenyys uudella jäsenyystasolla. Jäsenyyteen ei tule myöskään vaihtaa käyttäjää tai työryhmää, vaan kaikki muutokset merkitään päättämällä jäsenyys ja luomalla uusi oikeilla tiedoilla. Vain kirjausvirheet saa tehdä muuttamalla jäsenyystietoa.


