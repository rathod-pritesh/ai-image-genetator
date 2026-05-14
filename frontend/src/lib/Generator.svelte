<script>
  export let prompt = "";
  export let loading = false;
  export let error = "";
  export let generateImage; 
  export let handleKeyDown; 
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col gap-2">
    <label for="prompt" class="text-sm font-semibold text-gray-700"
      >Prompt</label
    >
    <textarea
      id="prompt"
      rows="3"
      class="w-full border border-gray-300 rounded-xl px-4 py-3 focus:ring-2 focus:ring-indigo-500 transition-all outline-none resize-none"
      placeholder="Describe your image and press Enter..."
      bind:value={prompt}
      on:keydown={handleKeyDown}
    ></textarea>
  </div>

  {#if error}
    <div
      class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-xl text-sm flex items-center gap-2"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5 text-red-500"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
          clip-rule="evenodd"
        />
      </svg>
      {error}
    </div>
  {/if}

  <button
    class="w-full bg-indigo-600 hover:bg-indigo-700 disabled:bg-indigo-300 text-white font-bold py-3 px-6 rounded-xl transition-colors flex items-center justify-center gap-2"
    on:click={generateImage}
    disabled={loading || !prompt}
  >
    {#if loading}
      <span
        class="animate-spin border-2 border-white border-t-transparent rounded-full w-5 h-5"
      ></span>
      Forging...
    {:else}
      Generate Image
    {/if}
  </button>
</div>
