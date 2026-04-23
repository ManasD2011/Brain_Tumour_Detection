import Upload from "@/components/Upload";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-100 to-blue-50 flex flex-col items-center justify-center p-6">
      <h1 className="text-4xl font-bold text-blue-700 mb-6">
        Brain Tumor Detection System
      </h1>

      <p className="text-gray-600 mb-8 text-center max-w-md">
        Upload MRI scans to detect and visualize tumor regions using
        AI-powered segmentation.
      </p>

      <Upload />
    </main>
  );
}
