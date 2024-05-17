#include <WiFi.h>
#include <WiFiClient.h>
#include <TFT_eSPI.h> // For the TFT screen

// TFT screen pins
#define TFT_CS 5
#define TFT_DC 2
#define TFT_RST 15

TFT_eSPI tft = TFT_eSPI();

const char* ssid = "your_wifi_ssid";
const char* password = "your_wifi_password";

WiFiServer server(8080);

void setup() {
  Serial.begin(115200);

  // Initialize the TFT screen
  tft.begin();
  tft.setRotation(1);
  tft.fillScreen(TFT_BLACK);
  tft.setTextColor(TFT_WHITE);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status()!= WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.println("Starting server...");

  // Start the server
  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    String message = client.readStringUntil('\n');
    Serial.println(message);

    // Display the message on the TFT screen
    displayMessage(message);
  }
}

void displayMessage(String message) {
  // Clear the screen
  tft.fillScreen(TFT_BLACK);

  // Display the message
  tft.setTextSize(2);
  tft.setCursor(10, 10);
  tft.println(message);

  // Update the screen
  tft.pushImage(0, 0, 240, 320, tft.getBuffer());
}