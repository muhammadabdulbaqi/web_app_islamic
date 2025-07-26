document.addEventListener("DOMContentLoaded", () => {
  fetch("/api/prayer-times")
    .then(res => res.json())
    .then(data => {
      const list = `
        <ul>
          <li><strong>Fajr:</strong> ${data.Fajr}</li>
          <li><strong>Dhuhr:</strong> ${data.Dhuhr}</li>
          <li><strong>Asr:</strong> ${data.Asr}</li>
          <li><strong>Maghrib:</strong> ${data.Maghrib}</li>
          <li><strong>Isha:</strong> ${data.Isha}</li>
        </ul>
        <p><em>Date: ${data.date}</em></p>
      `;
      document.getElementById("prayer-times").innerHTML = list;
    })
    .catch(err => {
      document.getElementById("prayer-times").innerHTML = "Could not load prayer times.";
      console.error("Error fetching prayer times:", err);
    });
});
