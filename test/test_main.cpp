#include <gtest/gtest.h>
#include "version.h"

TEST(VersionTest, ReturnsCorrectVersion) {
    EXPECT_EQ(GreenMind::getVersion(), "GreenMind v0.1.0");
}

TEST(VersionTest, NotEmpty) {
    EXPECT_FALSE(GreenMind::getVersion().empty());
}

// Main gtest standard
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
