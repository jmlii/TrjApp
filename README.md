# Työryhmäjäsenyydet

[Linkki sovellukseen Herokussa](https://jmlii-trjapp.herokuapp.com/)


## Tietokantasovelluksen aihekuvaus

Organisaatiossa on käytössä yhteistyöalusta, jossa on omia työtiloja eri työryhmille. Työntekijät voivat kuulua useisiin eri työryhmiin, ja työryhmissä on useita jäseniä. Työryhmän jäsenillä voi olla eri tasoisia oikeuksia työryhmän toimintoihin: selaaja (reader), muokkaaja (editor), hallinnoija (manager). Lisäksi kullakin työryhmällä on nimetty hyväksyjä, joka hyväksyy uusia henkilöitä ryhmän jäseneksi. Organisaatiossa tarvitaan tietokanta, josta pääsee helposti tarkistamaan, keitä kuhunkin työryhmään kuuluu ja minkä tason oikeudet kullakin käyttäjällä materiaaliin on, ja henkilöittäin mihin kaikkiin työryhmiin henkilö kuuluu ja minkä tason oikeuksin. Myöhempää kehittämistyötä varten tietokanta tulee rakentaa siten, että siitä on mahdollista saada tiedot myös jo päättyneiltä ajanjaksoilta niin käyttäjittäin kuin työryhmittäin hakemalla, milloin kukakin työntekijä on kuulunut mihinkin työryhmään ja millaisin oikeuksin. 

Tietokannan tarkastelujärjestelmällä on käyttäjiä, joiden tulee kirjautua järjestelmään tarkastellakseen tai muokatakseen tietoja. Tietokantaan on kahden tasoisia oikeuksia: tarkastelijat ja pääkäyttäjät. Tarkastelijat voivat vain selata järjestelmässä olevia tietoja ja tehdä käyttöikeushakemuksia. Pääkäyttäjät voivat lisätä järjestelmään uusia käyttäjiä ja poistaa niitä, muokata käyttäjien tietoja, lisätä, muokata ja poistaa työryhmiä, lisätä henkilöitä työryhmiin, muokata työryhmäjäsenten oikeustasoja ja poistaa henkilöitä työryhmistä. Kaikki työryhmiin kuuluvat henkilöt ovat myös järjestelmän käyttäjiä. Tietokannan käyttäjien ei kuitenkaan ole välttämätöntä olla työryhmien jäseniä. 

Käyttäjät pystyvät myös hakemaan käyttöoikeuksia uusiin työryhmiin, työryhmään olevan oikeustason muutosta tai oikeuksien poistoa. Oikeuspyynnöt hyväksytetään erikseen työryhmän hyväksyjällä, ja pääkäyttäjät merkitsevät hakemuksen tilan sen mukaisesti ja tekevät muutokset tietokantaan. 


## Toimintoja

* kirjautuminen 
* tietokantajärjestelmän käyttäjien lisääminen, muokkaaminen ja päättäminen (käyttäjän nimi, id, käyttöoikeustaso, aktiivinen (kyllä/ei), milloin lisätty järjestelmään, mihin asti käyttöoikeus ollut voimassa)
* työryhmän lisääminen, sen tietojen muokkaus ja päättäminen (työryhmän nimi, käyttöoikeushyväksyjä, aktiivinen (kyllä/ei) perustamisajankohta, työryhmän päättymispäivä jos työ päättynyt)
* käyttäjän työryhmän jäseneksi lisääminen ja poistaminen (työryhmän käyttöoikeustaso, lisäämisajankohta, poistamisajankohta) ja oikeustason muuttaminen
* työryhmien perustietojen listaaminen
* työryhmien jäsentietojen selaaminen
* järjestelmän käyttäjien listaaminen
* käyttäjän jäsenyystietojen selaaminen
* jäsenyyden hakeminen työryhmään tai muutoksen hakeminen työryhmään olevaan jäsenyystasoon tai jäsenyyden poiston hakeminen
* jäsenyyshakemusten selaaminen (avoimet ja suljetut) ja hyväksyminen tai hylkääminen sekä toteutetuksi merkitseminen.

[Linkki tarkempiin käyttötapauksiin](../master/documentation/kayttotapaukset.md) 

### Testitunnus sovelluksen testaamiseen
käyttäjätunnus: testaaja
salasana: salasana

## Tietokantakaavio

![](https://github.com/jmlii/TrjApp/raw/master/documentation/Tietokantakaavio.png "Tietokantakaavio")


[Linkki tietokantakaavioon (pdf)](../master/documentation/Tietokantakaavio.pdf)



