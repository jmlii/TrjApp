# TrjApp: Asennusohje

Tässä ohjeessa kuvataan työryhmäjäsenyyksien hallintaan tarkoitetun TrjApp-sovelluksen asennusohjeet ja käytön aloittaminen.

## Sovelluksen tiedostojen lataaminen

Lataa projekti koneellesi GitHubista tai kloonaa se omaan repositorioosi projektin repositoriosta osoitteesta https://github.com/jmlii/TrjApp. 

Kloonaa repositorio: Ota repositorion git-linkki talteen, siirry komentorivillä haluamaasi kansioon ja luo kopio repositoriosta komennolla `git clone kopioimasi_osoite`.

TAI

Lataa ZIP-tiedostona: Tallenna ladattava zip-tiedosto ja pura sen sisältö koneella haluamaasi paikkaan.

## Asennus ja käytön aloittaminen paikallisessa ympäristössä

Siirry terminaalissa / komentorivillä sovelluksen sisältävään kansioon. Luo sen sisälle Python-virtuaaliympäristö komennolla `python3 -m venv venv` ja aktivoi se komennolla `source venv/bin/activate`.

Asenna projektin riippuvuudet documents-kansion requirements.txt-tiedostosta ajamalla komento `pip install -r requirements.txt`.

Käynnistä sovellus sovelluksen sisältävästä kansiosta komennolla `python3 run.py`. Sovellusta voi käyttää paikallisesti selaimessa osoitteessa http://127.0.0.1:5000/. 

Sovelluksen ensimmäinen käynnistyskerta luo sovelluksen käyttämän paikallisen tietokannan (trj.db) ja sen luokat. Lisäksi ensimmäinen käynnistyskerta luo sovellukseen käyttäjätasot "admin" ja "basic" sekä yhden pääkäyttäjätunnuksen, jolla sovellukseen pääsee kirjautumaan (käyttäjätunnus "adminadmin", salasana "1q2w3e4r"). Tunnuksella voi luoda muut tarvittavat tunnukset, ja kun pääkäyttäjä on luonut oman tunnuksen, voi oletustunnuksen halutessaan poistaa.   

Sovelluksen tietokantaa pystyy käyttämään suoraan sovelluksesta. Tarvittaessa sitä voi käyttää komentoriviltä. Paikallisesti tietokanta käyttää SQLite3:a. Tietokanta tallentuu sovelluksen application-kansioon. Avaa tietokanta komentorivillä kansiosta komennolla `sqlite3 trj.db`.Näet tietokannan mallin komennolla `.schema`.


## Asennus ja käyttö Herokusta

Jotta sovelluksen voi asentaa Herokuun, tulee asentajalla olla Herokun käyttäjätunnus, käytössään Git ja välineet Herokun käyttöön komentoriviltä. Tunnuksen voi luoda osoitteessa https://signup.heroku.com/. Herokun omalla sivulla on ohjeet komentorivikäytöstä: [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). Herokuun tulee lisätä sovellus joko Herokussa omassa profiilissa tai komentoriviltä.

Herokussa uusi sovellus perustetaan oman profiilin sivulla olevan painikkeen New valikosta toiminnolla Create new app. Sovellukselle annetaan nimi ja maantieteellinen alue, ja se perustetaan painikkeella Create app. 
Komentorivillä sovellus perustetaan komennolla `heroku create sovelluksen_nimi` (vaihda tekstin sovelluksen_nimi tilalle haluamasi nimi). Heroku luo samalla sovellukselle Git-osoitteen.

Sovelluksen voi lähettää Herokuun Gitin avulla joko suoraan omalta koneelta tai GitHub-integraatiolla. Jos haluat käyttää GitHubia, tulee sovelluksen tiedostojen olla GitHub-repositoriossa, johon luodaan yhteys Herokun sovelluksesta. Asentajalla tulee tällöin olla käytössään myös GitHub-tunnus ja hänen tulee tuoda sovellus GitHub-repositorioon.

Omalta koneelta lähetettäessä käytetään Herokun luomaa Git-osoitetta. Herokun Git-osoite lisätään ensin tiedoksi paikalliseen versionhallintaan komennolla `git remote add heroku https://git.heroku.com/sovelluksen_nimi.git`. Tämän jälkeen projektin tiedoston lisätään commitiksi ja se lähetetään Herokuun komennolla `git push heroku master`. 

GitHub-integraatiota käytettäessä tulee luoda yhteys Heroku-sovelluksen ja GitHub-repositorion välille. Mene Herokussa sovelluksen tietojen Deploy-välilehdelle, kohtaan Connect to GitHub. Kirjoita kenttiin GitHub-tunnus ja repositorion nimi. Tunnistaudu GitHub-tunnuksellasi, ja yhteys on luotu. Jos olet tekemässä sovellukseen muutoksia, kannattaa ottaa käyttöön päivitysten automaattinen lataaminen (automatic deploys from GitHub). 

Kun sovellus on lähetetty Herokuun, tulee sille vielä lisätä Herokuun tietokanta. Tietokanta lisätään komentorivillä komennolla `heroku addons:add heroku-postgresql:hobby-dev`. 

Lisättyäsi tietokannan Herokun käyttöön, avaa sovellus Herokussa. Sovelluksen ensimmäinen käynnistyskerta luo Herokun tietokantaan sovelluksen tietokantataulut, oletuskäyttäjätasot ja yhden pääkäyttäjätasoisen käyttäjän, kuten paikallisesti käytettäessä. Tarvittaessa tietokantaa voi käyttää komentoriviltä. Heroku käyttää PostgreSQL:ää. Avaa Herokun käyttämä PostgreSQL-tietokanta komennolla `heroku phttps://devcenter.heroku.com/articles/heroku-clg:psql`. 
