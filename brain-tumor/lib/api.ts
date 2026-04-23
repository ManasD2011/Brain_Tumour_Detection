const API_URL = "http://127.0.0.1:8000";

export async function predict(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_URL}/predict`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error("Prediction failed");
  }

  return res.json();
}

