# TrjApp: Käyttöohje

Tässä ohjeessa opastetaan työryhmäjäsenyyksien hallintaan tarkoitetun TrjApp-sovelluksen käyttöä. Sovelluksella ylläpidetään tietoja tästä sovelluksesta erillisen yhteistyöalustan työryhmien työtilojen käyttöoikeuksista. Sovellukseen lisätään tiedot työryhmistä sekä työryhmien jäsenistä ja näiden käyttöoikeustasoista. Sovelluksesta pääsee tarkistamaan, mitä työryhmiä on, kuka hyväksyy työryhmän käyttöoikeudet, ja keitä kuuluu mihinkin työryhmiin. Lisäksi sovelluksessa on toiminto työryhmäjäsenyyksien hakemiseen, jolla käyttäjä pyytää lisäämään hänelle oikean tasoiset oikeudet työryhmiin, joissa hän on jäsenenä. 

Ohjeessa oletetaan, että sovellus on asennettu Herokuun asennusohjeen mukaisella tavalla, ja että sitä käytetään Heroku-sovelluksena. 

## Kirjautuminen

Siirry sovelluksen internetsivulle osoitteeseen, jonka olet saanut organisaatiosi pääkäyttäjältä. Jos et ole saanut käyttäjätunnusta, pyydä pääkäyttäjää luomaan sinulle tunnus ja salasana. 

Mallisovellus on osoitteessa https://jmlii-trjapp.herokuapp.com/. Testikäyttöön tarkoitetut tunnukset ovat: 
* Peruskäyttäjä: käyttäjätunnus "perustesti", salasana "salasana"
* Pääkäyttäjä: käyttäjätunnus "admintesti", salasana "salasana"

Kun lopetat sovelluksen käytön, kirjaudu ulos sivuston vasemman ylälaidan Kirjaudu ulos -painikkeesta.

## Peruskäyttäjän ohjeet

Kirjaudu sovellukseen avaamalla kirjautumissivu sivun oikean ylälaidan Kirjaudu-linkistä. Anna saamasi käyttäjätunnus ja salasana niille varattuihin kenttiin ja paina Kirjaudu-painiketta.

### Työryhmien selaaminen
Sivuston ylälaidan valikon linkistä "Selaa työryhmiä" pääset selaamaan työryhmien perustietoja. 

### Työryhmäjäsenyyden hakeminen
Sivuston ylälaidan valikon otsikkoa "Työryhmäjäsenyydet" klikkaamalla saat auki valikon, josta löytyvät toiminnot työryhmäjäsenyyden hakemiseen ja omien hakemustesi listaamiseen.

Hae jäsenyyttä -linkistä saat auki lomakkeen, jolla voit hakea uutta jäsenyyttä työryhmään, muutosta olemassa olevaan jäsenyystasoosi ja työryhmäjäsenyyden poistoa. Valitse ensin hakemuksen tyyppi (uusi rooli, muokkaus tai poisto). Hae sitten työryhmä-pudotusvalikosta haluamasi työryhmä, ja rooli-valikosta tarvitsemasi rooli työryhmään. Rooli määrittelee käyttöoikeuksien laajuutta työryhmän materiaaliin. Lopuksi kuvaile perustelut-kenttään lyhyesti, miksi tarvitset kyseisiä oikeuksia, tai miksi oikeudet saa ottaa pois. Paina lopuksi Lähetä pyyntö -painiketta, jolloin pyyntö tallentuu järjestelmään ja siirtyy pääkäyttäjän käsiteltäväksi.

Omat hakemuksesi -linkistä pääset selaamaan omia hakemuksiasi. Näet keskeneräisten hakemusten käsittelyn tilan sekä kaikki suljetut hakemukset.



## Pääkäyttäjän ohjeet

Jos sinulla on sovellukseen pääkäyttäjän oikeudet, näet sivuston ylälaidan valikossa enemmän toimintoja kuin peruskäyttäjä. Pääkäyttäjän valikossa kaksi ensimmäistä otsikkoa ovat samat kuin peruskäyttäjällä: Selaa työryhmiä ja Työryhmäjäsenyydet. Näiden lisäksi pääkäyttäjällä on valikot Ylläpitäjän toiminnot ja Tietokannan rakenteet.

### Ylläpitäjän toiminnot

#### Käyttäjien hallinta

Listaa käyttäjät -linkistä saat auki raportin sovelluksen käyttäjistä. Jokaiseen käyttäjään liittyy painikkeet Muuta epäaktiiviseksi ja Poista käyttäjä. Käyttäjä muutetaan epäaktiiviseksi, jos hänellä ei ole aktiivisia työryhmäjäsenyyksiä eikä enää tarvetta sovelluksen käytölle. Tällöin käyttäjän tiedot säilyvät tietokannassa, mutta hän ei pysty kirjautumaan sovellukseen ja käyttämään sitä. Jos käyttäjä poistetaan, niin kaikki häneen liittyvät tiedot poistuvat samalla tietokannasta. Käyttäjä poistetaan vain, jos hänen tietojaan ei enää tarvita tai jos hänen henkilötietojensa käyttöön ei enää ole lupaa.

Lisää uusi käyttäjä -linkistä voit lisätä sovellukselle uuden käyttäjän. Käyttäjästä on tallennettava etu- ja sukunimi, käyttäjätunnus, salasana ja sovelluksen käyttäjätaso. Kaikki työryhmien jäseninä olevat henkilöt on lisättävä myös sovelluksen käyttäjiksi, vaikka he eivät aktiivisesti käyttäisi sovellusta.


#### Työryhmien hallinta

Listaa työryhmät -linkistä saat auki raportin työryhmistä. Jokaiseen ryhmään liittyy painikkeet Muokkaa tietoja ja Lopeta työryhmä. Työryhmän muokkaamislomakkeella voit muuttaa työryhmän nimeä, käyttöoikeushyväksyjää ja tietoa työryhmän aktiivisuudesta. Työryhmän voi lopettaa joko muokkauslomakkeelta tai Lopeta työryhmä -painikkeesta. Työryhmä merkitään tällöin epäaktiiviseksi, mutta sen tiedot jäävät tietokantaan. Työryhmän voi palauttaa aktiiviseksi merkitsemällä sen jälleen aktiiviseksi muokkaamislomakkeella. Tallenna muutokset Päivitä työryhmän tiedot -painikkeella.

Työryhmien listaussivulla näet myös, kuinka monta uutta tai hyväksyttyä, oikeuksien lisäämistä ja hakemuksen loppukäsittelyä odottavaa jäsenyyspyyntöä järjestelmässä on mihinkin työryhmään.

Lisää uusi työryhmä -linkistä voit lisätä tietokantaan uuden työryhmän. Työryhmälle on annettava nimi ja sille on merkittävä oikeushyväksyjä, jolla hyväksytetään kaikki kyseisen työryhmän jäsenyysmuutokset. Tallenna uusi työryhmä Lisää työryhmä -painikkeella.


#### Jäsenyyshakemuksien hallinta
 
Listaa jäsenyyshakemukset -linkistä saat auki raportin jäsenyyshakemuksista. Jokaiseen hakemukseen liittyy painikkeet Merkitse hyväksytyksi, Merkitse hylätyksi ja Merkitse toteutetuksi. Kun työryhmän käyttöoikeushyväksyjältä on tarkistettu, saako haetun muutoksen tehdä, merkitään hakemus joko hyväksytyksi tai hylätyksi. Kun käyttäjä on liitetty yhteistyöalustassa työryhmään oikealla oikeustasolla, ja hänelle on lisätty nämä tiedot TrjApp-sovelluksen tietokantaan, merkitään hakemus toteutetuksi.

Lisää uusi jäsenyyshakemus toiselle käyttäjälle -linkistä pääkäyttäjä pääsee tekemään jäsenyyshakemuksen toisen käyttäjän puolesta. Lomake on muuten vastaava kuin itselle tehtävässä hakemuksessa, mutta siinä annetaan lisäksi tieto käyttäjästä, jolle oikeuksia haetaan.


### Tietokannan rakenteet


#### Työryhmien roolien hallinta

Listaa työryhmien roolit -linkistä saat auki raportin rooleista eli jäsenyystasoista, joita käyttäjillä voi olla yhteistyöalusta työryhmien työtiloihin. Listasta voit myös poistaa sellaiset roolit, joita ei enää ole käytössä. 

Lisää uusi rooli -linkistä voit lisätä tietokantaan rooleja eli jäsenyystasoja, joita käyttäjillä voi olla työryhmien työtiloihin. Sovelluksen käyttöönoton yhteydessä tulee lisätä kaikki ne roolit, joita organisaatiolla on käytössä. Jos rooleja otetaan myöhemmin käyttöön lisää, voit lisätä uusia rooleja.



#### Sovelluksen käyttäjätasojen hallinta

HUOM. Tämän osion toimintoja tulee käyttää vain harkiten, sillä ne vaikuttavat suoraan sovelluksen käyttöön!

Listaa sovelluksen käyttäjätasot -linkistä saat auki raportin sovelluksen käyttäjätasoja. Jos sovellus on asetettu asennusohjeen mukaisesti, on tietokannassa ainakin taso "admin" pääkäyttäjälle. 

Lisää uusi käyttäjätaso -linkistä voit lisätä tietokantaan uusia käyttäjätasoja sovelluksen käyttöön. Jos sovelluksella on pääkäyttäjien lisäksi myös peruskäyttäjiä, tulee se lisätä käyttäjätasoksi. Käyttäjätason admin on oltava juuri tällä nimellä, mutta muut tasot voit nimetä sopivaksi katsomallasi tavalla, sillä sovelluksen ohjelmakoodissa ei ole viittauksia niihin. Jos haluat ottaa käyttöön muita kuin pää- ja peruskäyttäjätasot, joudut muuttamaan myös ohjelmakoodia, jotta saat aidosti käyttöön eri tasoisia oikeuksia.


