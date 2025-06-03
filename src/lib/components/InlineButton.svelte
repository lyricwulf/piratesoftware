<script lang="ts">
  import { Button } from "$lib/components/ui/button";
  import { ArrowRight } from "@lucide/svelte";

  const {
    Icon = ArrowRight,
    children,
    class: className = "",
    iconPosition = "right",
    ...restProps
  } = $props();
</script>

<div class="popup-container w-fit">
  <Button
    variant="ghost"
    class="popup-small text-sm rounded-lg cursor-pointer font-bold flex
   items-center gap-2 softborder whitespace-normal h-auto min-h-9 text-start"
    {...restProps}
  >
    {#if Icon && iconPosition === "left"}
      <Icon size={18} />
    {/if}
    <div class="caption grow shrink-0 basis-0">
      {@render children()}
    </div>
    {#if Icon && iconPosition === "right"}
      <Icon size={18} />
    {/if}
  </Button>
</div>
