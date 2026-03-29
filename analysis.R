# Install if needed
if (!require(ggplot2)) install.packages("ggplot2")
# install.packages("dplyr")   # run once if not installed
library(dplyr)
library(ggplot2)

# Load data
data6 <- read.csv("data/stadium_simulation_data_6_turnstiles.csv",
                  header = TRUE, stringsAsFactors = FALSE)

# ---- CONFIG ----
interval_minutes <- 5
interval_sec <- interval_minutes * 60

# ---- TRANSFORM ----
data6_grouped <- data6 %>%
  mutate(
    arrival_time_sec = as.numeric(arrival_time),
    time_bin = floor(arrival_time_sec / interval_sec) * interval_sec
  ) %>%
  group_by(time_bin) %>%
  summarise(
    total_wait_sec = mean(total_wait, na.rm = TRUE)  # keep original clear
  ) %>%
  mutate(
    arrival_time = as.POSIXct(time_bin, origin = "1970-01-01", tz = "UTC"),
    total_wait_min = total_wait_sec / 60  # explicit naming
  )


# ---- PLOT ----
p6 <- ggplot(data6_grouped, aes(x = arrival_time, y = total_wait_min)) +
  geom_col(fill = "steelblue") +  # 🎨 color added
  scale_x_datetime(date_labels = "%H:%M") +
  labs(
    title = "Tickets Sold: 5,000 Turnstiles: 6",
    x = "Time (HH:MM)",
    y = "Wait Before Seated (minutes)"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 0, hjust = 1))

# ---- SAVE PNG ----
ggsave(
  filename = "six_turnstiles-5000_people.png",
  plot = p6,
  width = 10,
  height = 6,
  dpi = 300
)



# summary(data6)


data7 <- read.csv("data/stadium_simulation_data_7_turnstiles.csv", header=TRUE, stringsAsFactors=FALSE)

# ---- TRANSFORM ----
data7_grouped <- data7 %>%
  mutate(
    arrival_time_sec = as.numeric(arrival_time),
    time_bin = floor(arrival_time_sec / interval_sec) * interval_sec
  ) %>%
  group_by(time_bin) %>%
  summarise(
    total_wait_sec = mean(total_wait, na.rm = TRUE)  # keep original clear
  ) %>%
  mutate(
    arrival_time = as.POSIXct(time_bin, origin = "1970-01-01", tz = "UTC"),
    total_wait_min = total_wait_sec / 60  # explicit naming
  )


# ---- PLOT ----
p7 <- ggplot(data7_grouped, aes(x = arrival_time, y = total_wait_min)) +
  geom_col(fill = "steelblue") +  # 🎨 color added
  scale_x_datetime(date_labels = "%H:%M") +
  labs(
    title = "Tickets Sold: 5,000 Turnstiles: 7",
    x = "Time (HH:MM)",
    y = "Wait Before Seated (minutes)"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 0, hjust = 1))

# ---- SAVE PNG ----
ggsave(
  filename = "seven_turnstiles-5000_people.png",
  plot = p7,
  width = 10,
  height = 6,
  dpi = 300
)


# summary(data7)

data8 <- read.csv("data/stadium_simulation_data_8_turnstiles.csv", header=TRUE, stringsAsFactors=FALSE)

# ---- TRANSFORM ----
data8_grouped <- data8 %>%
  mutate(
    arrival_time_sec = as.numeric(arrival_time),
    time_bin = floor(arrival_time_sec / interval_sec) * interval_sec
  ) %>%
  group_by(time_bin) %>%
  summarise(
    total_wait_sec = mean(total_wait, na.rm = TRUE)  # keep original clear
  ) %>%
  mutate(
    arrival_time = as.POSIXct(time_bin, origin = "1970-01-01", tz = "UTC"),
    total_wait_min = total_wait_sec / 60  # explicit naming
  )


# ---- PLOT ----
p8 <- ggplot(data8_grouped, aes(x = arrival_time, y = total_wait_min)) +
  geom_col(fill = "steelblue") +  # 🎨 color added
  scale_x_datetime(date_labels = "%H:%M") +
  labs(
    title = "Tickets Sold: 5,000 Turnstiles: 8",
    x = "Time (HH:MM)",
    y = "Wait Before Seated (minutes)"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 0, hjust = 1))

# ---- SAVE PNG ----
ggsave(
  filename = "eight_turnstiles-5000_people.png",
  plot = p8,
  width = 10,
  height = 6,
  dpi = 300
)



# summary(data8)


data9 <- read.csv("data/stadium_simulation_data_6_turnstiles_80000_tickets_sold_10_access_points.csv", header=TRUE, stringsAsFactors=FALSE)

# ---- TRANSFORM ----
data9_grouped <- data9 %>%
  mutate(
    arrival_time_sec = as.numeric(arrival_time),
    time_bin = floor(arrival_time_sec / interval_sec) * interval_sec
  ) %>%
  group_by(time_bin) %>%
  summarise(
    total_wait_sec = mean(total_wait, na.rm = TRUE)  # keep original clear
  ) %>%
  mutate(
    arrival_time = as.POSIXct(time_bin, origin = "1970-01-01", tz = "UTC"),
    total_wait_min = total_wait_sec / 60  # explicit naming
  )


# ---- PLOT ----
p9 <- ggplot(data9_grouped, aes(x = arrival_time, y = total_wait_min)) +
  geom_col(fill = "steelblue") +  # 🎨 color added
  scale_x_datetime(date_labels = "%H:%M") +
  labs(
    title = "Tickets Sold: 80,000 Acess Points: 10 Turnstiles: 6 per AP",
    x = "Time (HH:MM)",
    y = "Wait Before Seated (minutes)"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 0, hjust = 1))

# ---- SAVE PNG ----
ggsave(
  filename = "six_turnstiles-80000_people_10_APs.png",
  plot = p9,
  width = 10,
  height = 6,
  dpi = 300
)


# summary(data9)


data10 <- read.csv("data/stadium_simulation_data_7_turnstiles_80000_tickets_sold_10_access_points.csv", header=TRUE, stringsAsFactors=FALSE)

# ---- TRANSFORM ----
data10_grouped <- data10 %>%
  mutate(
    arrival_time_sec = as.numeric(arrival_time),
    time_bin = floor(arrival_time_sec / interval_sec) * interval_sec
  ) %>%
  group_by(time_bin) %>%
  summarise(
    total_wait_sec = mean(total_wait, na.rm = TRUE)  # keep original clear
  ) %>%
  mutate(
    arrival_time = as.POSIXct(time_bin, origin = "1970-01-01", tz = "UTC"),
    total_wait_min = total_wait_sec / 60  # explicit naming
  )


# ---- PLOT ----
p10 <- ggplot(data10_grouped, aes(x = arrival_time, y = total_wait_min)) +
  geom_col(fill = "steelblue") +  # 🎨 color added
  scale_x_datetime(date_labels = "%H:%M") +
  labs(
    title = "Tickets Sold: 80,000 Acess Points: 10 Turnstiles: 7 per AP",
    x = "Time (HH:MM)",
    y = "Wait Before Seated (minutes)"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 0, hjust = 1))

# ---- SAVE PNG ----
ggsave(
  filename = "seven_turnstiles-80000_people_10_APs.png",
  plot = p10,
  width = 10,
  height = 6,
  dpi = 300
)

# summary(data10)


data11 <- read.csv("data/stadium_simulation_data_8_turnstiles_80000_tickets_sold_10_access_points.csv", header=TRUE, stringsAsFactors=FALSE)

# ---- TRANSFORM ----
data11_grouped <- data11 %>%
  mutate(
    arrival_time_sec = as.numeric(arrival_time),
    time_bin = floor(arrival_time_sec / interval_sec) * interval_sec
  ) %>%
  group_by(time_bin) %>%
  summarise(
    total_wait_sec = mean(total_wait, na.rm = TRUE)  # keep original clear
  ) %>%
  mutate(
    arrival_time = as.POSIXct(time_bin, origin = "1970-01-01", tz = "UTC"),
    total_wait_min = total_wait_sec / 60  # explicit naming
  )


# ---- PLOT ----
p11 <- ggplot(data11_grouped, aes(x = arrival_time, y = total_wait_min)) +
  geom_col(fill = "steelblue") +  # 🎨 color added
  scale_x_datetime(date_labels = "%H:%M") +
  labs(
    title = "Tickets Sold: 80,000 Acess Points: 10 Turnstiles: 8 per AP",
    x = "Time (HH:MM)",
    y = "Wait Before Seated (minutes)"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 0, hjust = 1))

# ---- SAVE PNG ----
ggsave(
  filename = "eight_turnstiles-80000_people_10_APs.png",
  plot = p11,
  width = 10,
  height = 6,
  dpi = 300
)

# summary(data11)


