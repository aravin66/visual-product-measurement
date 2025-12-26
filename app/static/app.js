async function analyze() {
    const textarea = document.getElementById("imageUrls");
    const output = document.getElementById("output");
    const loading = document.getElementById("loading");

    const urls = textarea.value
        .split("\n")
        .map(u => u.trim())
        .filter(u => u.length > 0);

    if (urls.length === 0) {
        output.textContent = "❌ Please enter at least one image URL.";
        return;
    }

    output.textContent = "";
    loading.classList.remove("hidden");

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ image_urls: urls })
        });

        const data = await response.json();

        loading.classList.add("hidden");
        output.textContent = JSON.stringify(data, null, 2);

    } catch (err) {
        loading.classList.add("hidden");
        output.textContent = "❌ Error occurred while analyzing images.";
    }
}
