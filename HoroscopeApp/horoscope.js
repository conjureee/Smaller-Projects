let month = "October".toLowerCase();
let horoscope = '';
let random_fortune = '';
let fortunes = [
  "Today brings unexpected opportunities your way.",
  "A surprise encounter will change your perspective.",
  "Trust your intuition - it will guide you well.",
  "Success comes to those who take bold action now.",
  "An old friend will bring important news soon."
];

random_fortune = fortunes[Math.floor(Math.random() * (fortunes.length-1))];

if (month == "january") horoscope = "♑Capricorn";
else if (month == "february") horoscope = "♒Aquarius";
else if (month == "march") horoscope = "♓Pisces";
else if (month == "april") horoscope = "♈Aries";
else if (month == "may") horoscope = "♉Taurus";
else if (month == "june") horoscope = "♊Gemini";
else if (month == "july") horoscope = "♋Cancer";
else if (month == "august") horoscope = "♌Leo";
else if (month == "september") horoscope = "♍Virgo";
else if (month == "october") horoscope = "♎Libra";
else if (month == "november") horoscope = "♏Scorpio";
else if (month == "december") horoscope = "♐Sagittarius";
else console.log("Incorrect month");

let h1 = document.querySelector("h1");
h1.textContent = `Based on your birth month, your horoscope is probably ${horoscope}... Here's a fortune for ya: ${random_fortune}`;