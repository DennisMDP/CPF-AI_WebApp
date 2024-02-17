// Funktion zum Abrufen und Aktualisieren des Bildes
function updateImage(url) {
    // Hier sollte der Code zum Abrufen des Bildes von Ihrer REST-API stehen
    // Dies kann mithilfe von Fetch-API oder XMLHttpRequest erfolgen
    fetch(url)
        .then(response => response.blob()) // Die Antwort als Blob abrufen
        .then(blob => {
            // URL zum Blob erstellen
            const imageUrl = URL.createObjectURL(blob);
            // Bildelement im DOM finden und das Bild aktualisieren
            document.getElementById('qualitycamImage').src = imageUrl;
        })
        .catch(error => console.error('Failed to load image from ' + url, error));
}

// Ein JavaScript-Objekt für die Zuordnung von data zu Texten erstellen
const textMapping = {
    "handyschale": "Handyschale",
    "handyschale_umgedreht": "Handyschale gewendet",
    "handyschale_falsch": "Handyschale falsch herum!",
    "leer": "Leerer Teileträger",
    "schokolade": "Schokoladenbox",
    "gummibaer": "Gummibärenbox"
};

// Funktion zum Abrufen der Daten von der REST-API und Anzeigen im Frontend
function updateLabel(url) {
    // Daten von der API abrufen
    fetch(url)
        .then(response => response.json()) // Die Antwort als JSON analysieren
        .then(data => {
            // Überprüfen, ob der Wert von data in der Zuordnung vorhanden ist
            if (textMapping.hasOwnProperty(data)) {
                // Den entsprechenden Text aus dem Objekt abrufen und in das Element mit der ID 'textContainer' einfügen
                document.getElementById('classLabel').innerHTML = textMapping[data];
            } else {
                // Wenn der Wert von data nicht in der Zuordnung vorhanden ist, kannst du hier einen Standardtext festlegen oder nichts tun
                console.log("No associated text for: " + data);
            }
        })
        .catch(error => console.error('Failed to get data from ' + url, error));
}

// Funktion, um die updateImage-Funktion und die fetchDataAndUpdateLabel-Funktion alle 2 Sekunden aufzurufen
function startUpdate() {
    const imgUrl = 'http://192.168.0.50/image.bmp'
    const apiUrl = 'URL_DER_LABEL_REST_API';
    // Die updateImage-Funktion einmal ausführen, wenn die Seite geladen wird
    updateImage(imgUrl);
    // Die fetchDataAndUpdateLabel-Funktion einmal ausführen, wenn die Seite geladen wird
    updateLabel(apiUrl);
    // Die updateImage-Funktion und die fetchDataAndUpdateLabel-Funktion alle 2 Sekunden wiederholen
    setInterval(() => {
        updateImage(imgUrl);
        updateLabel(apiUrl);
    }, 1000);
}

// Eventlistener, um die startUpdate-Funktion aufzurufen, wenn das DOM vollständig geladen ist
document.addEventListener('DOMContentLoaded', startUpdate);
