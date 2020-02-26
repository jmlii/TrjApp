# TrjApp: Käyttöohje

Tässä ohjeessa opastetaan työryhmäjäsenyyksien hallintaan tarkoitetun TrjApp-sovelluksen käyttöä. Sovelluksella ylläpidetään tietoja tästä sovelluksesta erillisen yhteistyöalustan työryhmien työtilojen tai muun aineiston käyttöoikeuksista. Sovellukseen lisätään tiedot työryhmistä sekä työryhmien jäsenistä ja näiden käyttöoikeustasoista. Sovelluksesta pääsee tarkistamaan, mitä työryhmiä on, kuka hyväksyy työryhmän käyttöoikeudet, ja keitä kuuluu mihinkin työryhmiin. Lisäksi sovelluksessa on toiminto työryhmäjäsenyyksien hakemiseen, jolla käyttäjä pyytää lisäämään hänelle oikean tasoiset oikeudet työryhmiin, joissa hän on jäsenenä. 

Ohjeessa oletetaan, että sovellus on asennettu Herokuun asennusohjeen mukaisella tavalla, ja että sitä käytetään Heroku-sovelluksena. 

## Kirjautuminen

Siirry sovelluksen internetsivulle osoitteeseen, jonka olet saanut pääkäyttäjältä. Jos et ole saanut käyttäjätunnusta, pyydä pääkäyttäjää luomaan sinulle tunnus ja salasana. 

Mallisovellus on osoitteessa https://jmlii-trjapp.herokuapp.com/. Testikäyttöön tarkoitetut tunnukset ovat: 
* Peruskäyttäjä: käyttäjätunnus "perustesti", salasana "salasana"
* Pääkäyttäjä: käyttäjätunnus "admintesti", salasana "salasana"

Kun lopetat sovelluksen käytön, kirjaudu ulos sivuston vasemman ylälaidan Kirjaudu ulos -painikkeesta.

## Peruskäyttäjän ohjeet

Kirjaudu sovellukseen avaamalla kirjautumissivu sivun oikean ylälaidan Kirjaudu-linkistä. Anna saamasi käyttäjätunnus ja salasana niille varattuihin kenttiin ja paina Kirjaudu-painiketta.

### Työryhmien selaaminen
Sivuston ylälaidan valikon linkistä Työryhmät pääset selaamaan työryhmien perustietoja. Näet työryhmien nimet sekä käyttöoikeuksien hyväksyjän. Näytä jäsenet -painikkesta avautuu lista työryhmän jäsenistä. 

### Työryhmäjäsenyyden hakeminen tai oman jäsenyyden muuttaminen tai poistaminen
Sivuston ylälaidan valikon otsikkoa "Työryhmäjäsenyydet" klikkaamalla saat auki valikon, josta löytyvät toiminnot omien työryhmiesi listaamiseen, työryhmäjäsenyyden hakemiseen, jäsenyyden muuttamiseen ja poistamiseen, ja omien hakemustesi listaamiseen.

Omat jäsenyydet -linkistä saat auki listan työryhmistä, joihin sinut on liitetty jäseneksi, roolisi (oikeustasosi) kussakin työryhmässä sekä kyseisen jäsenyyden alkamisajankohdasta.

Hae tai muokkaa jäsenyyttä -linkistä saat auki lomakkeen, jolla voit hakea uutta jäsenyyttä työryhmään, muutosta olemassa olevaan jäsenyystasoosi ja työryhmäjäsenyyden poistoa. Valitse ensin hakemuksen tyyppi (uusi rooli, muokkaus tai poisto). Hae sitten työryhmä-pudotusvalikosta haluamasi työryhmä, ja rooli-valikosta tarvitsemasi rooli työryhmään. Rooli määrittelee käyttöoikeuksien laajuutta työryhmän materiaaliin. Lopuksi kuvaile perustelut-kenttään lyhyesti, miksi tarvitset kyseisiä oikeuksia, tai miksi oikeudet saa ottaa pois. Paina lopuksi Lähetä pyyntö -painiketta, jolloin pyyntö tallentuu järjestelmään ja siirtyy pääkäyttäjien käsiteltäväksi.

Omat hakemuksesi -linkistä pääset selaamaan omia hakemuksiasi. Näet keskeneräisten hakemusten käsittelyn tilan sekä kaikki suljetut hakemukset.

## Pääkäyttäjän ohjeet

Jos sinulla on sovellukseen pääkäyttäjän oikeudet, näet sivuston ylälaidan valikossa enemmän toimintoja kuin peruskäyttäjä. Pääkäyttäjän valikossa kaksi ensimmäistä otsikkoa ovat samat kuin peruskäyttäjällä: Selaa työryhmiä ja Työryhmäjäsenyydet. Näiden lisäksi pääkäyttäjällä on valikot Ylläpitäjän toiminnot ja Tietokannan rakenteet.

### Ylläpitäjän toiminnot

#### Käyttäjien hallinta

Käyttäjät-linkistä saat auki raportin sovelluksen käyttäjistä ja listan kunkin käyttäjän työryhmäjäsenyyksien lukumäärästä. Käyttäjäraportilla jokaiseen käyttäjään liittyy painikkeet Päivitä tietoja, Työryhmät ja Poista käyttäjän tiedot. 

Päivitä tietoja -painikkeesta avautuu lomake käyttäjän tietojen muuttamiseen. Lomakkeella voit muuttaa käyttäjän nimiä ja käyttäjätasoa sekä merkitä tunnuksen aktiiviseksi tai epäaktiiviseksi. Käyttäjä muutetaan epäaktiiviseksi, jos hänellä ei ole aktiivisia työryhmäjäsenyyksiä eikä enää tarvetta sovelluksen käytölle. Tällöin käyttäjän tiedot säilyvät tietokannassa, mutta hän ei pysty kirjautumaan sovellukseen ja käyttämään sitä. Tallenna muutokset Päivitä käyttäjän tiedot -painikkeella. Jos haluat muuttaa käyttäjän salasanaa, pääset salansanan vaihtamislomakkeelle Vaihda salasana -linkistä.

Työryhmät-painikkeesta saat auki listan käyttäjän työryhmäjäsenyyksistä. Lista on vastaava kuin käyttäjien listaus omista työryhmistään.

Poista käyttäjän tiedot -painikkeella voi poistaa käyttäjän tiedot. Jos käyttäjä poistetaan, niin kaikki häneen liittyvät tiedot poistuvat tietokannasta, myös kaikki käyttäjän tekemät jäsenyyshakemukset ja jäsenyydet. Käyttäjä poistetaan vain, jos siihen on erityinen syy, esimerkiksi jos hänen tietonsa on poistettava tietosuojasyistä. Tilanteessa jossa käyttäjän henkilötietojen käyttöön ei ole lupaa, ensisijainen toimenpide on kuitenkin tietojen anonymisointi. Pääsääntöisesti käyttäjän tiedot jätetään tietokantaan,jotta siellä säilyy historiatieto työryhmien jäsenistä eri aikoina.  

Sovellukseen voi lisätä uuden käyttäjän joko valikon tai käyttäjäraportin Lisää uusi käyttäjä -linkistä. Käyttäjästä on tallennettava etu- ja sukunimi, käyttäjätunnus, salasana ja sovelluksen käyttäjätaso. Käyttäjä lisätään oletuksena aktiiviseksi. Kaikki työryhmien jäseninä olevat henkilöt on lisättävä myös sovelluksen aktiivisiksi käyttäjiksi, vaikka he eivät käyttäisi sovellusta.


#### Työryhmien hallinta

Työryhmät-linkistä saat auki raportin työryhmistä sekä listaukset työryhmien uusien ja käsittelyä odottavien jäsenyyspyyntöjen lukumääristä ja työryhmien jäsenmääristä. Työryhmäraportilla jokaiseen ryhmään liittyy painikkeet Päivitä tietoja, Näytä jäsenet ja Lopeta työryhmä. 

Työryhmän tietojen päivityslomakkeella voit muuttaa työryhmän nimeä, käyttöoikeushyväksyjää ja tietoa työryhmän aktiivisuudesta. Jos työryhmä lopetetaan, niin siinä olevat jäsenyydet päätetään ja työryhmä merkitään epäaktiiviseksi. Työryhmän perustiedot jäävät tietokantaan. Työryhmän voi palauttaa aktiiviseksi merkitsemällä sen jälleen aktiiviseksi muokkaamislomakkeella. Tallenna muutokset Päivitä työryhmän tiedot -painikkeella.

Näytä jäsenet -painikkeesta saat auki listan työryhmien jäsenistä. 

Lopeta työryhmä -painikkeella voit suoraan työryhmäraportillta merkitä työryhmän epäaktiiviseksi, kuten päivityslomakkeella.

Sovellukseen voi lisätä uuden työryhmän joko valikon tai työryhmäraportin Lisää uusi työryhmä -linkistä. Työryhmälle on annettava nimi ja sille on merkittävä oikeushyväksyjä, jolla hyväksytetään kaikki kyseisen työryhmän jäsenyysmuutokset. Tallenna uusi työryhmä Lisää työryhmä -painikkeella.


#### Jäsenyyshakemuksien hallinta
 
Jäsenyyshakemukset-linkistä saat auki raportin avoimista jäsenyyshakemuksista. Sivulla voit myös siirtyä tarkastelemaan suljettuja tai kaikkia hakemuksia. Avoimiin hakemuksiin liittyvät painikkeet Hyväksytty, Hylätty, Toteutettu, Muokkaa ja Poista. Kun työryhmän käyttöoikeushyväksyjältä on tarkistettu, saako haetun muutoksen tehdä, merkitään hakemus joko hyväksytyksi tai hylätyksi. Kun käyttäjä on liitetty yhteistyöalustassa työryhmään oikealla oikeustasolla, ja hänelle on lisätty nämä tiedot TrjApp-sovelluksen tietokantaan, merkitään hakemus toteutetuksi. Kaikki hylätyty hakemukset sulkeutuvat järjestelmästä heti. Hyväksytyt hakemukset sulkeutuvat, kun ne on merkitty myös toteutetuksi. Hakemusta voi muokata, jos käyttäjä on lähettänyt virheellisen hakemuksen. Hakemuksen voi poistaa, jos käyttäjä on lähettänyt turhan hakemuksen. Myös toteutetuksi merkittyjä hakemuksia voi muokata tai ne voidaan poistaa tarvittaessa. 

Lisää uusi jäsenyyshakemus toiselle käyttäjälle -linkistä pääkäyttäjä pääsee tekemään jäsenyyshakemuksen toisen käyttäjän puolesta. Lomake on muuten vastaava kuin itselle tehtävässä hakemuksessa, mutta siinä annetaan lisäksi tieto käyttäjästä, jolle oikeuksia haetaan.

#### Työryhmäjäsenyyksien hallinta

Työryhmäjäsenyydet-linkistä saat auki raportin kaikista jäsenyyksistä, sekä aktiivisista että päättyneistä. Jos jäsenyys on aktiivinen, siihen on liitetty painike Merkitse päättyneeksi, jolla jäsenyyden voi päättää. Tietokantaan tallentuu tällöin tieto jäsenyyden päättymisajankohdasta. Jäsenyys merkitään päättyneeksi, kun käyttäjä tekee pyynnön oikeuksien poistosta tai jos työryhmän käyttöoikeushyväksyjältä saadaan tieto, että käyttäjä tulee poistaa. Jos käyttäjä ei ole itse tehnyt poistopyyntöä, niin pääkäyttäjä voi tehdä sen. Kaikista poistoista tulee löytyä hakemus jäsenyyspyynnöistä. Samoin toimitaan jos käyttäjä hakee muutosta rooliin, joka hänellä on jossain työryhmässä, tai jos työryhmän käyttöoikeushyväksyjä pyytää tekemään muutoksen. Tällöin voimassa oleva jäsenyys päätetään, ja sen jälkeen lisätään uusi jäsenyys uutta roolia vastaavilla tiedoilla. 

Uusi työryhmäjäsenyys tallennetaan joko valikon tai työryhmäjäsenyysraportin Lisää uusi jäsenyys -linkistä. Lomakkeen pudotusvalikoista valitaan käyttäjä, työryhmä ja rooli, ja jäsenyys lisätään tallenna jäsenyys -painikkeella. Kun jäsenyys on lisätty, tulee vielä käydä sulkemassa sitä vastaava jäsenyyshakemus merkitsemällä se käsitellyksi. 


### Tietokannan rakenteet


#### Työryhmien roolien hallinta

Työryhmien roolit -linkistä saat auki raportin rooleista eli jäsenyystasoista, joita käyttäjillä voi olla yhteistyöalustan työryhmien työtiloihin tai aineistoihin. Listasta voit myös poistaa turhat roolit. Jäsenyyshakemuksissa tai työryhmäjäsenyyksissä käytössä olevia rooleja ei voi poistaa. 

Lisää uusi rooli -linkistä voit lisätä tietokantaan rooleja eli jäsenyystasoja, joita käyttäjillä voi olla työryhmien työtiloihin. Sovelluksen käyttöönoton yhteydessä tulee lisätä kaikki ne roolit, joita organisaatiolla on käytössä. Jos rooleja otetaan myöhemmin käyttöön lisää, voit lisätä uusia rooleja.



#### Sovelluksen käyttäjätasojen hallinta

HUOM. Tämän osion toimintoja tulee käyttää vain harkiten, sillä ne vaikuttavat suoraan sovelluksen käyttöön!

Sovelluksen käyttäjätasot -linkistä saat auki raportin sovelluksen käyttäjätasoja. Jos sovellus on asetettu asennusohjeen mukaisesti, on tietokannassa ainakin tasot "admin" pääkäyttäjälle ja "basic" peruskäyttäjälle. Voit poistaa käyttäjätason, jos se ei ole käytössä yhdelläkään käyttäjällä. 

Lisää uusi käyttäjätaso -linkistä voit lisätä tietokantaan uusia käyttäjätasoja sovelluksen käyttöön. Käyttäjätason admin on oltava juuri tällä nimellä, mutta muut tasot voit nimetä sopivaksi katsomallasi tavalla, sillä sovelluksen ohjelmakoodissa ei ole viittauksia niihin. Jos haluat ottaa käyttöön muita kuin pää- ja peruskäyttäjätasot, joudut muuttamaan myös ohjelmakoodia, jotta saat aidosti käyttöön eri tasoisia oikeuksia.



