import { useTheme } from "@/components/theme-provider";
import { Monitor, Moon, Sun } from "lucide-react";

function ThemeToggle() {
  const { theme, setTheme } = useTheme();

  const options = [
    { value: "light", label: "Light", icon: <Sun size="16" /> },
    { value: "dark", label: "Dark", icon: <Moon size="16" /> },
    { value: "system", label: "System", icon: <Monitor size="16" /> },
  ] as const;

  return (
    <div className="bg-muted flex items-center gap-0.5 rounded-sm p-1">
      {options.map((opt) => {
        const active = theme === opt.value;

        return (
          <button
            key={opt.value}
            onClick={() => setTheme(opt.value)}
            title={opt.label}
            className={`item-center flex rounded p-1 ${
              active
                ? "bg-background dark:bg-border text-foreground shadow-sm"
                : "text-muted-foreground hover:bg-background/50"
            } `}
          >
            {opt.icon}
            <span className="hidden">{opt.label}</span>
          </button>
        );
      })}
    </div>
  );
}

export { ThemeToggle };
