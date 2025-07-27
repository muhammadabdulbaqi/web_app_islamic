document.addEventListener("DOMContentLoaded", async () => {
  const select = document.getElementById("surah-select");
  const surahInfoDiv = document.getElementById("surah-info");
  const versesDiv = document.getElementById("verses");

  let quran = [];
  let metadata = [];

  try {
    // Load Quran text
    const quranRes = await fetch("/api/quran");
    const quranData = await quranRes.json();
    quran = quranData.quran;

    // Load metadata
    const metaRes = await fetch("/api/quran/metadata");
    const metaData = await metaRes.json();
    metadata = metaData.metadata;

    // Clear the initial "Loading..." option
    select.innerHTML = "";

    // Populate Surah dropdown
    metadata.forEach((surah, index) => {
      const option = document.createElement("option");
      option.value = index + 1; // surah number (1-based)
      option.textContent = `${index + 1}. ${surah.english_name}`;
      select.appendChild(option);
    });

    // Auto-load Surah 1 by default
    select.value = "1";
    loadSurah(1);

    // Handle Surah selection
    select.addEventListener("change", () => {
      const selectedSurah = parseInt(select.value);
      if (!selectedSurah) return;
      loadSurah(selectedSurah);
    });

    function loadSurah(surahNum) {
      const meta = metadata[surahNum - 1];
      const start = meta.start_ayah;
      const count = meta.ayah_count;

      const filteredVerses = quran.slice(start - 1, start - 1 + count);

      surahInfoDiv.innerHTML = `
        <h2>${meta.english_name} (${meta.arabic_name})</h2>
        <p><strong>Type:</strong> ${meta.type}, <strong>Verses:</strong> ${meta.ayah_count}</p>
      `;

      versesDiv.innerHTML = filteredVerses.map((v, idx) => `
        <div class="verse">
          <p><strong>${idx + 1}.</strong></p>
          <p><strong>Arabic:</strong> ${v.arabic}</p>
          <p><strong>English:</strong> ${v.english}</p>
        </div><hr>
      `).join("");
    }

  } catch (err) {
    console.error("Error loading Qur'an data:", err);
    versesDiv.innerHTML = "❌ Failed to load Qur'an data.";
  }
});
