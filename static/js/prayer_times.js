document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("address-input");
  const loadButton = document.getElementById("load-times");
  const prayerTimesDiv = document.getElementById("prayer-times");
  const nextPrayerDiv = document.getElementById("next-prayer");
  const cityDiv = document.getElementById("selected-city");

  const keysToShow = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"];

  async function fetchPrayerData(address) {
    try {
      const timesRes = await fetch(`/api/prayer-times?address=${encodeURIComponent(address)}`);
      const timesData = await timesRes.json();

      const timings = timesData.timings;
      const date = timesData.date;
      const city = timesData.city || address;

      // Show city
      cityDiv.innerHTML = `<strong>Location:</strong> ${city}`;

      // Build prayer times list
      let timesHtml = `<p><strong>Date:</strong> ${date}</p><ul>`;
      for (let [name, time] of Object.entries(timings)) {
        if (keysToShow.includes(name)) {
          timesHtml += `<li><strong>${name}:</strong> ${time}</li>`;
        }
      }
      timesHtml += `</ul>`;
      prayerTimesDiv.innerHTML = timesHtml;

      // Get next prayer
      const nextRes = await fetch(`/api/next-prayer?address=${encodeURIComponent(address)}`);
      const nextData = await nextRes.json();

      const nextName = nextData.name || "No more prayers today";
      const nextTime = nextData.time || "-";

      nextPrayerDiv.innerHTML = `
        <h2>Next Prayer</h2>
        <p><strong>${nextName}:</strong> ${nextTime}</p>
      `;
    } catch (err) {
      console.error("Error fetching prayer data:", err);
      prayerTimesDiv.innerHTML = "❌ Could not load prayer times.";
      nextPrayerDiv.innerHTML = "❌ Could not load next prayer.";
    }
  }

  loadButton.addEventListener("click", () => {
    const address = input.value.trim();
    if (!address) {
      alert("Please enter a city or address.");
      return;
    }
    prayerTimesDiv.innerHTML = "Loading...";
    nextPrayerDiv.innerHTML = "Loading...";
    fetchPrayerData(address);
  });
});
