


# TrjApp-tietokantasovellus työryhmäjäsenyyksien hallintaan

[Linkki sovellukseen Herokussa](https://jmlii-trjapp.herokuapp.com/)


## Sovelluksen aihekuvaus

### Taustaksi 
Organisaatiossa on käytössä yhteistyöalusta, jossa on omia työtiloja eri työryhmille. Työntekijät voivat kuulua useisiin eri työryhmiin, ja työryhmissä on useita jäseniä. Työryhmän jäsenillä voi olla eri tasoisia oikeuksia työryhmän toimintoihin. Lisäksi kullakin työryhmällä on nimetty hyväksyjä, joka hyväksyy uusia henkilöitä ryhmän jäseneksi. Organisaatiossa tarvitaan tietokanta, josta pääsee helposti tarkistamaan, keitä kuhunkin työryhmään kuuluu ja minkä tason oikeudet kullakin käyttäjällä materiaaliin on, ja henkilöittäin mihin kaikkiin työryhmiin henkilö kuuluu ja minkä tason oikeuksin. Myöhempää kehittämistyötä varten tietokanta rakennettiin siten, että siitä on mahdollista saada tiedot myös jo päättyneiltä ajanjaksoilta niin käyttäjittäin kuin työryhmittäin hakemalla, milloin kukakin työntekijä on kuulunut mihinkin työryhmään ja millaisin oikeuksin. 

### TrjApp-sovelluksen esittely
Sovelluksella ylläpidetään tietoja organisaation työryhmistä ja työryhmien jäsenistä. Lisäksi sovelluksen kautta haetaan jäsenyyksiä työryhmiin eli käytännössä käyttöoikeuksia työryhmien aineistoihin, sekä tehdään muutos- ja poistopyyntöjä olemassa oleviin jäsenyyksiin. 

Käyttäjien tulee kirjautua sovellukseen nähdäkseen mitään sen tietoja.  

Sovellukseen on kahden tasoisia oikeuksia: perustaso ja pääkäyttäjät. Perustason käyttäjät voivat vain selata työryhmien tietoja ja jäseniä sekä omia jäsenyyksiään ja tehdä käyttöikeushakemuksia eli hakea jäsenyyttä työryhmiin, työryhmään olevan oikeustason muutosta tai oikeuksien poistoa. Pääkäyttäjät voivat lisätä järjestelmään uusia käyttäjiä, muokata käyttäjien tietoja ja poistaa ne, lisätä ja muokata työryhmiä, lisätä henkilöitä työryhmiin ja lopettaa työryhmän jäsenten jäsenyyksiä ja käsitellä jäsenyyshakemuksia. Pääkäyttäjät voivat myös tehdä jäsenyyshakemuksia muiden käyttäjien puolesta. Jäsenyyshakemukset hyväksytetään erikseen työryhmän hyväksyjällä, ja pääkäyttäjät merkitsevät hakemuksen tilan sen mukaisesti ja tekevät muutokset tietokantaan. Lisäksi pääkäyttäjät voivat lisätä järjestelmään työryhmien rooleja ja sovelluksen käyttöoikeustasoja, ja poistaa rooleja ja oikeustasoja jotka eivät ole käytössä.

Kaikki työryhmiin kuuluvat henkilöt ovat myös järjestelmän käyttäjiä. Sovelluksen käyttäjien ei kuitenkaan ole välttämätöntä olla työryhmien jäseniä. 

Sovelluksella ei voida määritellä sovelluksesta erillisen yhteistyöalustan tai muiden sen ulkopuolisten sovellusten käyttöoikeuksia, vaan sovellus on tarkoitettu vain tietojen ylläpitoon. Se ei sisällä mitään rajapintoja muihin sovelluksiin.

## Toimintoja

* kirjautuminen 
* käyttäjien lisääminen, muokkaaminen ja päättäminen tai poistaminen
* työryhmän lisääminen, sen tietojen muokkaus ja päättäminen
* käyttäjän työryhmän jäseneksi lisääminen ja jäsenyyden päättäminen; muutokset työryhmän rooleihin eli käyttöoikeustasoon tehdään päättämällä nykyinen jäsenyys ja lisäämällä uusi päivitetyillä tiedoilla
* työryhmien perustietojen listaaminen
* työryhmien jäsentietojen selaaminen
* järjestelmän käyttäjien listaaminen
* käyttäjän jäsenyystietojen selaaminen
* jäsenyyden hakeminen työryhmään tai muutoksen hakeminen työryhmään olevaan jäsenyystasoon tai jäsenyyden poiston hakeminen
* jäsenyyshakemusten selaaminen (avoimet ja suljetut) ja hyväksytyksi tai hylätyksi sekä toteutetuksi merkitseminen
* yhteistyöalustan käyttöoikeustasojen eli työryhmän roolien lisääminen ja poistaminen
* TrjApp-sovelluksen käyttöoikeustasojen lisääminen ja poistaminen tarvittaessa; sovelluksen oletusasennuksessa mukana tulevat perustaso ja pääkäyttäjätaso.

[Linkki tarkempiin käyttötapauksiin](../master/documentation/kayttotapaukset.md) 


## Asentaminen ja käyttäminen

[Linkki asennusohjeeseen](../master/documentation/asennusohje.md)

[Linkki käyttöohjeeseen](../master/documentation/kayttoohje.md)

### Testitunnukset sovelluksen testaamiseen Herokussa
**Peruskäyttäjä:**

käyttäjätunnus: perustesti

salasana: salasana

**Pääkäyttäjä:**

käyttäjätunnus: admintesti

salasana: salasana


## Tietokantakaavio

![](https://github.com/jmlii/TrjApp/raw/master/documentation/Tietokantakaavio.png "Tietokantakaavio")


## Jatkokehityskohteita
* Käyttäjän tietojen muokkaamisen muuttaminen siten, että käyttäjää ei voi merkitä epäaktiiviseksi, jos käyttäjällä on voimassa olevia työryhmäjäsenyyksiä.
* Työryhmän tietojen muokkaamisen muuttaminen siten, että työryhmää ei voi merkitä päättyneeksi ilman että kaikki sen jäsenyydet on ensin päätetty.
* Jäsenyyshakemusten listaan toiminto, josta pääsee suoraan lisäämään hyväksytyn hakemuksen mukaisen jäsenyyden tietokantaan.
* Tietojen automaattinen hävittäminen tietyn ajan kuluttua tietokohteiden päättämisestä, esim. työryhmän ja sen jäsenyyksien tietojen hävittäminen 10 vuotta työryhmän työn päättymisen jälkeen. 
