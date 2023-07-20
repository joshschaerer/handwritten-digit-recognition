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
});

// Initial position
let pos = { x: 0, y: 0 };

// Flag used to trigger drawing
let isDrawing = false;

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
};

/**
 * Function to draw on the canvas
 * @param {*} e Event
 */
const sketch = (e) => {
  if (!isDrawing) return;

  ctx.beginPath();
  ctx.lineWidth = 5;
  ctx.lineCap = "round";
  ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue(
    "--color-text"
  );

  ctx.moveTo(pos.x, pos.y);

  pos = getPos(e);

  ctx.lineTo(pos.x, pos.y);

  ctx.stroke();
};
