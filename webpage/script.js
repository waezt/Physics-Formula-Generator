document.getElementById("fetchBtn").addEventListener("click", async () => {
    const formulaElement = document.getElementById("formula");
    const explanationElement = document.getElementById("explanation");

    formulaElement.textContent = "Loading...";
    explanationElement.textContent = "";

    try {
        const response = await fetch("https://42rafeurq7.execute-api.eu-north-1.amazonaws.com/prod/get-formula");

        if (!response.ok) throw new Error("HTTP error " + response.status);

        const data = await response.json();

        formulaElement.textContent = data.formula || "No formula found";
        explanationElement.textContent = data.explanation || "";

    } catch (error) {
        console.error("Error fetching formula:", error);
        formulaElement.textContent = "Error loading formula.";
        explanationElement.textContent = "";
    }
});
