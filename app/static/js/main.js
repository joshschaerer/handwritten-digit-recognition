/*=============== APP ===============*/
// Access the list element
const list = document.getElementById("app-list");

/**
 * Helper function to reset all items
 */
const resetList = () => {
  for (let i = 0; i < list.childElementCount; i++) {
    const item = list.children[i];
    item.style.transform = `translateY(${100 * i}%)`;
    item.style.backgroundColor = `unset`;
    item.children.item(1).innerHTML = "0.00";
  }
};

// Setup all items
resetList();

/*=============== CANVAS ===============*/
// Access the canvas element
const canvas = document.getElementById("canvas");
// Access the canvas context
const ctx = canvas.getContext("2d");

// Wait for the content to load
// NOTE: This is considered best practice
window.addEventListener("load", function () {
  canvas.addEventListener("mousedown", engage);
  canvas.addEventListener("mousemove", sketch);
  canvas.addEventListener("mouseup", disengage);
  window.addEventListener("keyup", (e) => {
    if (e.key === "c") {
      resetList();
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  });
});

// Initial position
let pos = { x: 0, y: 0 };

// Flag used to trigger drawing
let isDrawing = false;

// Flag used to throttle the number of requests
let isFetching = false;

/**
 * Helper function to recognize the written digit
 */
const recognizeDigit = () => {
  // Toggle the flag
  isFetching = true;

  // Fetch recognized digits from ai model
  const options = {
    headers: { "Content-Type": "application/json" },
    method: "POST",
    body: JSON.stringify(canvas.toDataURL()),
  };
  fetch("/", options)
    .then((response) => response.json())
    .then((data) => {
      if (!data) return;

      // Sort the data
      // NOTE: Used to reorder list items
      const sorted = [...data[0]].sort((a, b) => b - a);
      for (let i = 0; i < data[0].length; i++) {
        // Access elements
        var item = document.getElementById(`item-${i}`);
        var parent = item.parentElement;

        // Update elements
        item.innerHTML = (data[0][i] * 100).toFixed(2);
        parent.style.transform = `translateY(${
          100 * sorted.indexOf(data[0][i])
        }%)`;
        parent.style.backgroundColor = `hsla(var(--color-green), ${data[0][i]})`;
      }
    });

  // Reset the flag
  // NOTE: Whilst throttling the number of requests
  setTimeout(() => {
    isFetching = false;
  }, 100);
};

/**
 * Helper function to get the current position
 * @param {*} e Event
 * @returns The current position
 */
const getPos = (e) => {
  return { x: e.offsetX, y: e.offsetY };
};

/**
 * Function to start drawing
 * @param {*} e Event
 */
const engage = (e) => {
  isDrawing = true;
  pos = getPos(e);
};

/**
 * Function to stop drawing
 */
const disengage = () => {
  isDrawing = false;
  recognizeDigit();
};

/**
 * Function to draw on the canvas
 * @param {*} e Event
 */
const sketch = (e) => {
  if (!isDrawing) return;

  // Define drawing style
  ctx.beginPath();
  ctx.lineWidth = 10;
  ctx.lineCap = "round";
  ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue(
    "--color-text"
  );

  // Detect key input
  // NOTE: Used to toggle between drawing and erasing
  ctx.globalCompositeOperation = "source-over"; // Default
  if (e.shiftKey) ctx.globalCompositeOperation = "destination-out";

  // Draw on canvas
  ctx.moveTo(pos.x, pos.y);
  pos = getPos(e);
  ctx.lineTo(pos.x, pos.y);
  ctx.stroke();

  // Recognize digit
  // NOTE: Also throttle number of requests
  if (isFetching) return;
  recognizeDigit();
};
