document.addEventListener('DOMContentLoaded', (event) => {
    const quoteElement = document.getElementById('quote');
    const quoteContainer = document.getElementById('quote-container');
    const quoteText = quoteElement.innerText.trim();
    const numberOfParts = 10;

    // Function to split the text into approximately equal parts by word boundaries
    function splitTextIntoParts(text, parts) {
        const words = text.split(' ');
        const partLength = Math.ceil(words.length / parts);
        const result = [];
        for (let i = 0; i < words.length; i += partLength) {
            result.push(words.slice(i, i + partLength).join(' '));
        }
        return result;
    }

    // Function to write part of the quote to the terminal
    function writeQuotePart(part) {
        const div = document.createElement('div');
        div.classList.add('typing-animation');
        div.innerText = part;
        quoteContainer.appendChild(div);
    }

    // Split the quote into parts by word boundaries
    const quoteParts = splitTextIntoParts(quoteText, numberOfParts);

    // Display each part at 1-second intervals
    quoteParts.forEach((part, index) => {
        setTimeout(() => {
            writeQuotePart(part);
        }, index * 1000);
    });
});
